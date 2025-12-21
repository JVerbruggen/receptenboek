from __future__ import annotations

import argparse
import json
import re
import unicodedata
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable, Optional


class ScriptExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._in_script = False
        self._script_type: Optional[str] = None
        self._script_id: Optional[str] = None
        self._buffer: list[str] = []
        self.scripts: list[tuple[Optional[str], Optional[str], str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        if tag.lower() != "script":
            return
        self._in_script = True
        self._script_type = None
        self._script_id = None
        for k, v in attrs:
            lk = k.lower()
            if lk == "type":
                self._script_type = v
            elif lk == "id":
                self._script_id = v
        self._buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "script" or not self._in_script:
            return
        content = "".join(self._buffer).strip()
        self.scripts.append((self._script_type, self._script_id, content))
        self._in_script = False
        self._script_type = None
        self._script_id = None
        self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._in_script:
            self._buffer.append(data)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = text.replace("&", " en ")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def _walk(obj: Any) -> Iterable[Any]:
    stack = [obj]
    while stack:
        cur = stack.pop()
        yield cur
        if isinstance(cur, dict):
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)


def _first_str(value: Any) -> Optional[str]:
    if isinstance(value, str) and value.strip():
        return value.strip()
    if isinstance(value, list):
        for item in value:
            s = _first_str(item)
            if s:
                return s
    return None


def _parse_json_maybe(text: str) -> Optional[Any]:
    text = text.strip()
    if not text:
        return None

    try:
        return json.loads(text)
    except Exception:
        return None


def _find_recipe_jsonld(script_content: str) -> list[dict[str, Any]]:
    parsed = _parse_json_maybe(script_content)
    if parsed is None:
        return []

    recipes: list[dict[str, Any]] = []

    for node in _walk(parsed):
        if isinstance(node, dict):
            t = node.get("@type")
            if t == "Recipe" or (isinstance(t, list) and "Recipe" in t):
                recipes.append(node)
    return recipes


def _extract_from_recipe_jsonld(recipe: dict[str, Any]) -> dict[str, Any]:
    title = _first_str(recipe.get("name")) or ""

    time = (
        _first_str(recipe.get("totalTime"))
        or _first_str(recipe.get("cookTime"))
        or _first_str(recipe.get("prepTime"))
        or ""
    )

    tags: list[str] = []
    for k in ("keywords", "recipeCategory", "recipeCuisine"):
        v = recipe.get(k)
        if isinstance(v, str):
            tags.extend([t.strip() for t in re.split(r"[,;]", v) if t.strip()])
        elif isinstance(v, list):
            tags.extend([str(x).strip() for x in v if str(x).strip()])
    tags = list(dict.fromkeys(tags))

    ingredients: list[dict[str, str]] = []
    for ing in recipe.get("recipeIngredient") or []:
        if not isinstance(ing, str):
            continue
        s = ing.strip()
        if not s:
            continue
        amount, name = split_ingredient_amount_name(s)
        ingredients.append({"name": name, "amount": amount})

    steps: list[str] = []
    instr = recipe.get("recipeInstructions")
    if isinstance(instr, str):
        steps = [s.strip() for s in re.split(r"\n+", instr) if s.strip()]
    elif isinstance(instr, list):
        for item in instr:
            if isinstance(item, str):
                if item.strip():
                    steps.append(item.strip())
            elif isinstance(item, dict):
                text = _first_str(item.get("text"))
                if text:
                    steps.append(text)

    image = ""
    img = recipe.get("image")
    if isinstance(img, str):
        image = img
    elif isinstance(img, list):
        image = _first_str(img) or ""
    elif isinstance(img, dict):
        image = _first_str(img.get("url")) or ""

    return {
        "title": title,
        "time": time,
        "tags": tags,
        "ingredients": ingredients,
        "steps": steps,
        "image_url": image,
    }


_AMOUNT_PREFIX_RE = re.compile(
    r"^(?P<amount>(?:\d+[\d\s/.,-]*|½|¼|¾|\u00bd|\u00bc|\u00be)(?:\s*(?:g|kg|ml|l|el|tl|stuk\b|stuks\b|sneetjes\b|teen\b|tenen\b|bol\b|bollen\b|pak\b|zak\b|zakje\b|blik\b|blikken\b))?)(?:\s+)(?P<name>.+)$",
    flags=re.IGNORECASE,
)


def split_ingredient_amount_name(s: str) -> tuple[str, str]:
    s = re.sub(r"\s+", " ", s.strip())
    m = _AMOUNT_PREFIX_RE.match(s)
    if not m:
        return "", s
    amount = (m.group("amount") or "").strip()
    name = (m.group("name") or "").strip()
    return amount, name


def _extract_next_data(scripts: list[tuple[Optional[str], Optional[str], str]]) -> Optional[dict[str, Any]]:
    for t, sid, content in scripts:
        if sid == "__NEXT_DATA__" and content:
            parsed = _parse_json_maybe(content)
            if isinstance(parsed, dict):
                return parsed
    return None


def _find_best_recipe_obj_in_next_data(next_data: dict[str, Any]) -> Optional[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for node in _walk(next_data):
        if not isinstance(node, dict):
            continue

        if "recipe" in node and isinstance(node.get("recipe"), dict):
            candidates.append(node["recipe"])
            continue

        keys = set(node.keys())
        if ("name" in keys or "title" in keys) and ("ingredients" in keys or "recipeIngredient" in keys):
            candidates.append(node)

    def score(obj: dict[str, Any]) -> int:
        s = 0
        if _first_str(obj.get("name")) or _first_str(obj.get("title")):
            s += 3
        if obj.get("ingredients") or obj.get("recipeIngredient"):
            s += 3
        if obj.get("steps") or obj.get("instructions") or obj.get("recipeInstructions"):
            s += 3
        if obj.get("image") or obj.get("imageUrl") or obj.get("image_url"):
            s += 1
        return s

    if not candidates:
        return None
    candidates.sort(key=score, reverse=True)
    return candidates[0]


def _extract_from_next_data_recipe(obj: dict[str, Any]) -> dict[str, Any]:
    title = _first_str(obj.get("title")) or _first_str(obj.get("name")) or ""

    time = (
        _first_str(obj.get("time"))
        or _first_str(obj.get("totalTime"))
        or _first_str(obj.get("cookTime"))
        or _first_str(obj.get("prepTime"))
        or _first_str(obj.get("prepTimeRange"))
        or ""
    )

    tags: list[str] = []
    for k in ("tags", "labels", "badges", "keywords"):
        v = obj.get(k)
        if isinstance(v, list):
            for item in v:
                if isinstance(item, str) and item.strip():
                    tags.append(item.strip())
                elif isinstance(item, dict):
                    name = _first_str(item.get("name")) or _first_str(item.get("label"))
                    if name:
                        tags.append(name)
        elif isinstance(v, str) and v.strip():
            tags.extend([t.strip() for t in re.split(r"[,;]", v) if t.strip()])

    tags = list(dict.fromkeys(tags))

    ingredients: list[dict[str, str]] = []

    ing = obj.get("ingredients")
    if isinstance(ing, list):
        for item in ing:
            if isinstance(item, dict):
                name = _first_str(item.get("name")) or _first_str(item.get("ingredient")) or ""
                amount = (
                    _first_str(item.get("amount"))
                    or _first_str(item.get("quantity"))
                    or _first_str(item.get("quantityText"))
                    or _first_str(item.get("displayAmount"))
                    or ""
                )
                if name:
                    ingredients.append({"name": name, "amount": amount})
            elif isinstance(item, str) and item.strip():
                amount, name = split_ingredient_amount_name(item)
                ingredients.append({"name": name, "amount": amount})

    if not ingredients:
        for item in obj.get("recipeIngredient") or []:
            if isinstance(item, str) and item.strip():
                amount, name = split_ingredient_amount_name(item)
                ingredients.append({"name": name, "amount": amount})

    steps: list[str] = []
    for key in ("steps", "instructions", "method", "recipeInstructions"):
        v = obj.get(key)
        if isinstance(v, list) and v:
            for s in v:
                if isinstance(s, str) and s.strip():
                    steps.append(s.strip())
                elif isinstance(s, dict):
                    text = _first_str(s.get("text")) or _first_str(s.get("instruction"))
                    if text:
                        steps.append(text)
            if steps:
                break
        if isinstance(v, str) and v.strip():
            steps = [x.strip() for x in re.split(r"\n+", v) if x.strip()]
            break

    image_url = (
        _first_str(obj.get("image"))
        or _first_str(obj.get("imageUrl"))
        or _first_str(obj.get("image_url"))
        or ""
    )

    return {
        "title": title,
        "time": time,
        "tags": tags,
        "ingredients": ingredients,
        "steps": steps,
        "image_url": image_url,
    }


def _extract_labels_from_next_recipe_obj(obj: dict[str, Any]) -> list[str]:
    labels: list[str] = []

    raw_tags = obj.get("tags")
    if isinstance(raw_tags, list):
        for item in raw_tags:
            if not isinstance(item, dict):
                continue

            name = _first_str(item.get("name")) or _first_str(item.get("label"))
            slug = _first_str(item.get("slug"))
            tag_type = _first_str(item.get("type"))

            if (name or "").strip().lower() == "seo" or (slug or "").strip().lower() == "seo" or (tag_type or "").strip().lower() == "seo":
                continue

            prefs = item.get("preferences")
            if isinstance(prefs, list):
                for p in prefs:
                    if isinstance(p, str) and p.strip():
                        labels.append(p.strip())

            if item.get("displayLabel") is True and name:
                labels.append(name)

    return list(dict.fromkeys(labels))


_LABELS_RE = re.compile(
    r"Labels:\s*(?P<labels>.+?)(?:\s+Allergenen:|\s+Gemaakt in een fabriek|\s+Bereidingstijd)",
    flags=re.IGNORECASE | re.DOTALL,
)
_IMG_RE = re.compile(r"https?://media\.hellofresh\.com/[^\s\"')>]+\.jpe?g", flags=re.IGNORECASE)


def _extract_labels_from_html(html: str) -> list[str]:
    m = _LABELS_RE.search(html)
    if not m:
        return []
    raw = re.sub(r"\s+", " ", (m.group("labels") or "").strip())
    parts = [p.strip() for p in re.split(r"[•|]", raw) if p.strip()]
    return list(dict.fromkeys(parts))


def _extract_main_image_from_html(html: str) -> str:
    # Pick the first media.hellofresh.com jpg that looks like the main image (often has c_fit,.../image/...).
    m = _IMG_RE.search(html)
    return m.group(0) if m else ""


def _normalize_time_str(s: str) -> str:
    s = (s or "").strip()
    if not s:
        return ""
    # ISO 8601 duration like PT35M
    m = re.fullmatch(r"PT(?:(\d+)H)?(?:(\d+)M)?", s)
    if m:
        h = int(m.group(1) or 0)
        mins = int(m.group(2) or 0)
        total = h * 60 + mins
        return f"{total} min" if total else ""
    s = s.replace("minuten", "min").replace("minute", "min")
    s = re.sub(r"\s+", " ", s)
    # if it contains a plain number, keep it + 'min'
    m2 = re.search(r"(\d{1,3})\s*min", s, flags=re.IGNORECASE)
    if m2:
        return f"{m2.group(1)} min"
    m3 = re.fullmatch(r"(\d{1,3})\s*m", s, flags=re.IGNORECASE)
    if m3:
        return f"{m3.group(1)} min"
    return s


@dataclass
class RecipeResult:
    title: str
    slug: str
    time: str
    tags: list[str]
    labels: list[str]
    ingredients: list[dict[str, str]]
    steps: list[str]
    image_url: str


def extract_recipe_from_html(html: str, *, fallback_slug: Optional[str] = None) -> RecipeResult:
    parser = ScriptExtractor()
    parser.feed(html)

    next_data = _extract_next_data(parser.scripts)
    next_recipe_obj = _find_best_recipe_obj_in_next_data(next_data) if next_data else None
    next_extracted = _extract_from_next_data_recipe(next_recipe_obj) if next_recipe_obj else None

    jsonld_recipes: list[dict[str, Any]] = []
    for t, sid, content in parser.scripts:
        if t and t.lower() == "application/ld+json" and content:
            jsonld_recipes.extend(_find_recipe_jsonld(content))

    if jsonld_recipes:
        extracted = _extract_from_recipe_jsonld(jsonld_recipes[0])
    else:
        if not next_data:
            raise ValueError("No JSON-LD Recipe or __NEXT_DATA__ found")
        if not next_recipe_obj:
            raise ValueError("Could not locate recipe object in __NEXT_DATA__")
        extracted = _extract_from_next_data_recipe(next_recipe_obj)

    if next_extracted:
        # Prefer richer HF-specific tags/time from __NEXT_DATA__ but keep JSON-LD ingredients/steps.
        if not extracted.get("time") and next_extracted.get("time"):
            extracted["time"] = next_extracted["time"]
        if (not (extracted.get("tags") or [])) and next_extracted.get("tags"):
            extracted["tags"] = [t for t in (next_extracted.get("tags") or []) if isinstance(t, str) and t.strip()]
        if not extracted.get("image_url") and next_extracted.get("image_url"):
            extracted["image_url"] = next_extracted["image_url"]

    title = (extracted.get("title") or "").strip()
    if not title:
        raise ValueError("Missing title")

    slug = slugify(title)
    if not slug and fallback_slug:
        slug = fallback_slug

    time = _normalize_time_str(extracted.get("time") or "")
    tags = [t for t in (extracted.get("tags") or []) if isinstance(t, str) and t.strip()]

    ingredients = extracted.get("ingredients") or []
    if not isinstance(ingredients, list):
        ingredients = []

    steps = [s for s in (extracted.get("steps") or []) if isinstance(s, str) and s.strip()]

    labels = _extract_labels_from_next_recipe_obj(next_recipe_obj) if next_recipe_obj else []
    if not labels:
        labels = _extract_labels_from_html(html)
    image_url = (extracted.get("image_url") or "").strip() or _extract_main_image_from_html(html)

    return RecipeResult(
        title=title,
        slug=slug,
        time=time,
        tags=tags,
        labels=labels,
        ingredients=ingredients,
        steps=steps,
        image_url=image_url,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract HelloFresh recipe data from saved HTML pages")
    ap.add_argument("--in", dest="in_dir", default="raw/hellofresh", help="Input folder with .html files")
    ap.add_argument("--out", dest="out_file", default="assets/hellofresh_extracted.json", help="Output JSON file")
    ap.add_argument("--stdout", action="store_true", help="Print JSON to stdout")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON")

    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    out_file = Path(args.out_file)

    html_files = sorted([p for p in in_dir.glob("*.html") if p.is_file()])
    if not html_files:
        raise SystemExit(f"No .html files found in {in_dir}")

    results: list[dict[str, Any]] = []
    errors: list[str] = []

    for path in html_files:
        html = path.read_text(encoding="utf-8", errors="ignore")
        fallback_slug = slugify(path.stem)
        try:
            r = extract_recipe_from_html(html, fallback_slug=fallback_slug)
            results.append(
                {
                    "source_file": path.name,
                    "title": r.title,
                    "slug": r.slug,
                    "time": r.time,
                    "tags": r.tags,
                    "labels": r.labels,
                    "ingredients": r.ingredients,
                    "steps": r.steps,
                    "image_url": r.image_url,
                }
            )
        except Exception as e:
            errors.append(f"{path.name}: {e}")

    indent = 2 if args.pretty else None
    json_text = json.dumps(results, ensure_ascii=False, indent=indent)

    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json_text + "\n", encoding="utf-8")

    if args.stdout:
        print(json_text)

    if errors:
        raise SystemExit("Failed to parse some files:\n" + "\n".join(errors))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
