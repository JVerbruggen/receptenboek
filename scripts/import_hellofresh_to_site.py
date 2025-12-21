from __future__ import annotations

import argparse
import html as html_mod
import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _dedupe_cards_by_slug(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    def merge(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        title_a = str(a.get("title") or "").strip()
        title_b = str(b.get("title") or "").strip()
        slug = str(a.get("slug") or b.get("slug") or "").strip()

        time_a = str(a.get("time") or "").strip()
        time_b = str(b.get("time") or "").strip()

        image_a = str(a.get("image") or "").strip()
        image_b = str(b.get("image") or "").strip()

        tags_a = a.get("tags") if isinstance(a.get("tags"), list) else []
        tags_b = b.get("tags") if isinstance(b.get("tags"), list) else []
        merged_tags: list[str] = []
        for t in [*tags_a, *tags_b]:
            if isinstance(t, str):
                nt = _normalize_tag(t)
                if nt and nt not in merged_tags:
                    merged_tags.append(nt)

        return {
            "title": title_a or title_b,
            "slug": slug,
            "time": time_a or time_b,
            "tags": merged_tags,
            "image": image_a or image_b,
        }

    by_slug: dict[str, dict[str, Any]] = {}
    passthrough: list[dict[str, Any]] = []

    for card in cards:
        slug = str(card.get("slug") or "").strip()
        if not slug:
            passthrough.append(card)
            continue
        if slug in by_slug:
            by_slug[slug] = merge(by_slug[slug], card)
        else:
            by_slug[slug] = card

    return passthrough + list(by_slug.values())


def _normalize_tag(tag: str) -> str:
    t = tag.strip()
    if not t:
        return ""

    if t.lower() == "seo":
        return ""

    mapping = {
        "Calorie Smart": "Caloriebewust",
        "CalorieSmart": "Caloriebewust",
        "High Protein": "Eiwitrijk",
        "HighProtein": "Eiwitrijk",
        "Family": "Familie",
        "Veggie": "Veggie",
        "Vegetarian": "Veggie",
        "Plant-based": "Plant-based",
        "Plant Based": "Plant-based",
    }
    return mapping.get(t, t)


def _tags_from_recipe(recipe: dict[str, Any]) -> list[str]:
    tags: list[str] = []
    for src in ("labels", "tags"):
        for t in recipe.get(src) or []:
            if isinstance(t, str):
                nt = _normalize_tag(t)
                if nt and nt not in tags:
                    tags.append(nt)
    return tags


def _derive_url_slug(url: str) -> str:
    segment = re.sub(r"[?#].*$", "", url).rstrip("/").split("/")[-1]
    # strip trailing -<hex/id>
    segment = re.sub(r"-[0-9a-f]{16,}$", "", segment, flags=re.IGNORECASE)
    return segment


def _derive_file_slug(filename: str) -> str:
    name = filename
    if name.lower().endswith(".html"):
        name = name[:-5]
    # strip trailing -<hex/id>
    name = re.sub(r"-[0-9a-f]{16,}$", "", name, flags=re.IGNORECASE)
    return name


def _strip_html(s: str) -> str:
    if not s:
        return ""
    # Remove tags, then unescape entities.
    s = re.sub(r"<[^>]+>", " ", s)
    s = html_mod.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


_UNIT_PREFIX_RE = re.compile(
    r"^(?P<unit>stuk\(s\)|gram|kg|ml|l|el|tl)\s+(?P<name>.+)$", flags=re.IGNORECASE
)


def _normalize_ingredient(name: str, amount: str) -> tuple[str, str]:
    name = _strip_html(str(name or ""))
    amount = _strip_html(str(amount or ""))

    m = _UNIT_PREFIX_RE.match(name)
    if m and amount and re.fullmatch(r"[0-9]+(?:\.[0-9]+)?|½|¼|¾|\u00bd|\u00bc|\u00be", amount):
        unit = m.group("unit")
        proper_name = m.group("name").strip()
        return proper_name, f"{amount} {unit}"
    return name, amount


def _download(url: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        out_path.write_bytes(resp.read())


def _ext_from_url(url: str) -> str:
    base = re.sub(r"[?#].*$", "", url)
    m = re.search(r"\.(jpe?g|png|webp)$", base, flags=re.IGNORECASE)
    if not m:
        return ".jpg"
    return "." + m.group(1).lower().replace("jpeg", "jpg")


def _render_recipe_markdown(
    *,
    title: str,
    slug: str,
    time: str,
    tags: list[str],
    image_path: str,
    ingredients: list[dict[str, str]],
    steps: list[str],
    source_url: str,
) -> str:
    tags_line = ", ".join([t.lower() for t in tags if t])
    if tags_line:
        tags_line += "."

    time_display = time or "—"

    lines: list[str] = []
    lines.append(f"# {title} {{#{slug}}}")
    lines.append("")
    if image_path:
        lines.append(f"![{title}]({image_path})")
        lines.append("")
    lines.append(f"- Totale tijd: {time_display}.")
    if tags_line:
        lines.append(f"- {tags_line}")
    if source_url:
        lines.append(f"- Bron: {source_url}")
    lines.append("")
    lines.append("## Benodigdheden")
    lines.append("2 personen")
    lines.append("")
    lines.append("| Ingredient | Hoeveelheid |")
    lines.append("|------------|-------------|")
    for ing in ingredients:
        raw_name = ing.get("name") or ""
        raw_amount = ing.get("amount") or ""
        name, amount = _normalize_ingredient(raw_name, raw_amount)
        if not name:
            continue
        # Basic escaping for pipes
        name = name.replace("|", "\\|")
        amount = amount.replace("|", "\\|")
        lines.append(f"| {name} | {amount} |")

    lines.append("")
    for idx, step in enumerate(steps, start=1):
        step_text = _strip_html(step)
        lines.append(f"## {idx} Stap {idx}")
        lines.append(f"- {step_text}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _remove_old_stub_sections(index_text: str, urls: list[str]) -> str:
    text = index_text
    for url in urls:
        pos = text.find(url)
        if pos == -1:
            continue

        # Find the start of the recipe header preceding this URL
        start = text.rfind("\n# ", 0, pos)
        if start == -1:
            start = 0
        else:
            start += 1  # keep the leading newline

        # Find the end separator after this URL block
        end = text.find("\n---\n", pos)
        if end == -1:
            continue
        end = end + len("\n---\n")

        text = text[:start] + text[end:]

    return text


def _remove_sections_by_anchors(index_text: str, anchors: list[str]) -> str:
    text = index_text
    for anchor in anchors:
        token = "{" + f"#{anchor}" + "}"
        pos = text.find(token)
        if pos == -1:
            continue

        start = text.rfind("\n# ", 0, pos)
        if start == -1:
            start = 0
        else:
            start += 1

        end = text.find("\n---\n", pos)
        if end == -1:
            continue
        end = end + len("\n---\n")
        text = text[:start] + text[end:]

    return text


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Import extracted HelloFresh recipes into the site")
    ap.add_argument("--extracted", default="assets/hellofresh_extracted.json", help="Extractor output JSON")
    ap.add_argument("--recipes-json", default="assets/recipes.json", help="Card list JSON")
    ap.add_argument("--index", default="index.md", help="Index markdown")
    ap.add_argument("--images-dir", default="assets/images", help="Images output folder")
    ap.add_argument("--site-prefix", default="/receptenboek", help="Site path prefix")
    ap.add_argument("--urls-file", default="raw/hellofresh/urls.txt", help="URLs file used for stubs")
    args = ap.parse_args(argv)

    extracted_path = Path(args.extracted)
    recipes_json_path = Path(args.recipes_json)
    index_path = Path(args.index)
    images_dir = Path(args.images_dir)
    urls = [line.strip() for line in Path(args.urls_file).read_text(encoding="utf-8").splitlines() if line.strip()]

    extracted = _load_json(extracted_path)
    if not isinstance(extracted, list):
        print("Extractor output must be a list", file=sys.stderr)
        return 2

    recipes_cards = _load_json(recipes_json_path)
    if not isinstance(recipes_cards, list):
        print("recipes.json must be a list", file=sys.stderr)
        return 2

    # Remove old stubs (based on URL-derived slugs)
    stub_slugs = {_derive_url_slug(u) for u in urls}
    recipes_cards = [r for r in recipes_cards if str(r.get("slug") or "") not in stub_slugs]

    url_by_file_slug: dict[str, str] = {}
    for u in urls:
        url_by_file_slug[_derive_url_slug(u)] = u

    incoming_slugs: set[str] = {
        str(r.get("slug") or "").strip()
        for r in extracted
        if isinstance(r, dict) and str(r.get("slug") or "").strip()
    }

    # Make this script idempotent: remove any existing cards for recipes we are about to import.
    recipes_cards = [r for r in recipes_cards if str(r.get("slug") or "").strip() not in incoming_slugs]

    rendered_blocks: list[str] = []
    anchors: list[str] = []

    for r in extracted:
        title = str(r.get("title") or "").strip()
        slug = str(r.get("slug") or "").strip()
        if not title or not slug:
            continue

        anchors.append(slug)

        tags = _tags_from_recipe(r)
        time = str(r.get("time") or "").strip()

        image_url = str(r.get("image_url") or "").strip()
        image_path = ""
        if image_url:
            ext = _ext_from_url(image_url)
            local_name = slug + ext
            local_path = images_dir / local_name
            if not local_path.exists():
                _download(image_url, local_path)
            image_path = f"{args.site_prefix}/assets/images/{local_name}"

        card_entry = {
            "title": title,
            "slug": slug,
            "time": time,
            "tags": tags,
            "image": image_path,
        }
        recipes_cards.append(card_entry)

        source_url = ""
        source_file = str(r.get("source_file") or "").strip()
        if source_file:
            key = _derive_file_slug(source_file)
            source_url = url_by_file_slug.get(key, "")

        ingredients = r.get("ingredients") or []
        steps = r.get("steps") or []
        if not isinstance(ingredients, list):
            ingredients = []
        if not isinstance(steps, list):
            steps = []

        rendered_blocks.append(
            _render_recipe_markdown(
                title=title,
                slug=slug,
                time=time,
                tags=tags,
                image_path=image_path,
                ingredients=ingredients,
                steps=[str(s) for s in steps if isinstance(s, str) and str(s).strip()],
                source_url=source_url,
            )
        )

    recipes_cards = _dedupe_cards_by_slug(recipes_cards)
    # Sort cards by title for stable UI
    recipes_cards.sort(key=lambda x: str(x.get("title") or "").lower())
    _save_json(recipes_json_path, recipes_cards)

    index_text = index_path.read_text(encoding="utf-8")
    index_text = _remove_old_stub_sections(index_text, urls)
    index_text = _remove_sections_by_anchors(index_text, anchors)

    marker = "<!-- template -->"
    mi = index_text.find(marker)
    if mi == -1:
        print(f"Marker not found in {index_path}: {marker}", file=sys.stderr)
        return 2

    insert_at = index_text.rfind("\n", 0, mi)
    if insert_at == -1:
        insert_at = mi

    block_text = "\n".join(rendered_blocks) + "\n"

    index_text = index_text[:insert_at] + "\n" + block_text + index_text[insert_at:]
    index_path.write_text(index_text, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
