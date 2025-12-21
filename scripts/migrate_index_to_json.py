from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import argparse


ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "index.md"
RECIPES_JSON_PATH = ROOT / "assets" / "recipes.json"


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _read_text_from_git(rev: str, path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    out = subprocess.check_output(["git", "show", f"{rev}:{rel}"], cwd=str(ROOT))
    return out.decode("utf-8", errors="replace")


def _norm_title(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s


def _slugify(text: str) -> str:
    text = text.strip().lower()
    text = text.replace("&", " en ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


@dataclass
class ParsedRecipe:
    title: str
    slug: str
    time: str
    tags_line: str
    source: str
    servings_text: str
    servings: int | None
    ingredients: list[dict[str, str]]
    steps: list[dict[str, Any]]


_H1_RE = re.compile(r"^#\s+(?P<title>.*?)(?:\s+\{#(?P<slug>[^}]+)\})?\s*$")
_TIME_RE = re.compile(r"^-\s*Totale\s+tijd:\s*(?P<time>.+?)\.?\s*$", re.IGNORECASE)
_SOURCE_RE = re.compile(r"^-\s*Bron:\s*(?P<url>\S+)\s*$", re.IGNORECASE)


def _parse_block(block: str) -> ParsedRecipe:
    lines = [ln.rstrip("\n") for ln in block.splitlines()]
    # header
    title = ""
    slug = ""
    for ln in lines:
        m = _H1_RE.match(ln)
        if m:
            title = (m.group("title") or "").strip()
            slug = (m.group("slug") or "").strip()
            break
    if not title:
        raise ValueError("Missing title")
    if not slug:
        slug = _slugify(title)

    time = ""
    tags_line = ""
    source = ""
    for ln in lines:
        mt = _TIME_RE.match(ln)
        if mt and not time:
            time = (mt.group("time") or "").strip()
            continue
        ms = _SOURCE_RE.match(ln)
        if ms and not source:
            source = (ms.group("url") or "").strip()
            continue

        # tags line (best-effort): a bullet that is not time/bron
        if ln.startswith("-") and ("Totale tijd" not in ln) and ("Bron:" not in ln):
            cand = ln.lstrip("- ").strip()
            if cand and not tags_line:
                tags_line = cand.rstrip(".")

    # servings
    servings_text = ""
    servings: int | None = None
    for i, ln in enumerate(lines):
        if ln.strip().lower() == "## benodigdheden":
            # next non-empty line
            for j in range(i + 1, min(i + 6, len(lines))):
                t = lines[j].strip()
                if not t:
                    continue
                servings_text = t
                m = re.search(r"(\d+)", t)
                if m:
                    try:
                        servings = int(m.group(1))
                    except Exception:
                        servings = None
                break
            break

    # ingredients table
    ingredients: list[dict[str, str]] = []
    try:
        start = lines.index("| Ingredient | Hoeveelheid |")
    except ValueError:
        start = -1
    if start != -1:
        for ln in lines[start + 2 :]:
            if not ln.startswith("|"):
                # stop when table ends
                if ln.strip().startswith("## "):
                    break
                continue
            parts = [p.strip() for p in ln.strip("|").split("|")]
            if len(parts) < 2:
                continue
            name, amount = parts[0].replace("\\|", "|"), parts[1].replace("\\|", "|")
            if name.lower() == "ingredient" and amount.lower() == "hoeveelheid":
                continue
            if name and name != "------------":
                ingredients.append({"name": name, "amount": amount})

    # steps
    steps: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for ln in lines:
        if ln.startswith("## ") and ln.strip().lower() != "## benodigdheden":
            # new step
            if current:
                steps.append(current)
            current = {"title": ln[3:].strip(), "items": []}
            continue
        if current is not None:
            s = ln.strip()
            if s.startswith("-"):
                item = s.lstrip("- ").strip()
                if item:
                    current["items"].append(item)

    if current:
        steps.append(current)

    return ParsedRecipe(
        title=title,
        slug=slug,
        time=time,
        tags_line=tags_line,
        source=source,
        servings_text=servings_text,
        servings=servings,
        ingredients=ingredients,
        steps=steps,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Migrate recipe details from index.md into assets/recipes.json")
    parser.add_argument(
        "--git-rev",
        dest="git_rev",
        default=None,
        help="Read index.md content from a git revision (via `git show <rev>:index.md`).",
    )
    parser.add_argument(
        "--no-rewrite-index",
        dest="no_rewrite_index",
        action="store_true",
        help="Do not rewrite index.md (useful when reading from --git-rev).",
    )
    args = parser.parse_args(argv)

    if args.git_rev:
        index_text = _read_text_from_git(args.git_rev, INDEX_PATH)
        # Safety: default to not rewriting the working tree when input comes from git.
        args.no_rewrite_index = True
    else:
        index_text = INDEX_PATH.read_text(encoding="utf-8")
    cards = _load_json(RECIPES_JSON_PATH)
    if not isinstance(cards, list):
        raise SystemExit("assets/recipes.json must be a list")

    by_slug = {str(r.get("slug") or "").strip(): r for r in cards if isinstance(r, dict)}
    by_title = { _norm_title(str(r.get("title") or "")): r for r in cards if isinstance(r, dict) }

    # Extract recipe markdown blocks between "## 📖 Alle Recepten" and "<!-- template -->"
    start_anchor = "## 📖 Alle Recepten"
    end_anchor = "<!-- template -->"

    si = index_text.find(start_anchor)
    if si == -1:
        raise SystemExit(f"Could not find {start_anchor!r} in index.md")
    ei = index_text.find(end_anchor)
    if ei == -1:
        raise SystemExit(f"Could not find {end_anchor!r} in index.md")

    between = index_text[si:ei]

    # Find first recipe header after the anchor
    m = re.search(r"^#\s+", between, flags=re.MULTILINE)
    if not m:
        raise SystemExit("Could not find any recipe blocks after 'Alle Recepten'")

    recipes_md = between[m.start():]

    # Split on recipe headers (H1 '# ...') using boundaries rather than relying on '---' separators.
    # This is robust across versions where recipes are stacked without hr lines between them.
    normalized = recipes_md.replace("\r\n", "\n")

    h1_positions = [m.start() for m in re.finditer(r"^#\s+", normalized, flags=re.MULTILINE)]
    blocks: list[str] = []
    for idx, start in enumerate(h1_positions):
        end = h1_positions[idx + 1] if idx + 1 < len(h1_positions) else len(normalized)
        block = normalized[start:end].strip("\n")
        if block:
            blocks.append(block)

    parsed: list[ParsedRecipe] = []
    missing: list[str] = []

    for b in blocks:
        try:
            pr = _parse_block(b)
        except Exception as e:
            missing.append(f"Failed to parse block: {e}")
            continue
        parsed.append(pr)

        target = by_slug.get(pr.slug)
        if not target:
            target = by_title.get(_norm_title(pr.title))

        if not target:
            missing.append(f"No matching card in recipes.json for: {pr.title} ({pr.slug})")
            continue

        # write full recipe fields
        if pr.time and not str(target.get("time") or "").strip():
            target["time"] = pr.time

        if pr.source:
            target["source"] = pr.source

        if pr.servings is not None:
            target["servings"] = pr.servings
        if pr.servings_text:
            target["servings_text"] = pr.servings_text

        target["ingredients"] = pr.ingredients
        target["steps"] = pr.steps

    _save_json(RECIPES_JSON_PATH, cards)

    if not args.no_rewrite_index:
        # Rewrite index.md: keep content up to '## 📖 Alle Recepten', then add a JS-render target,
        # remove the old template block too.
        pre = index_text[: si + len(start_anchor)]
        post = index_text[ei:]

        # Strip the old template section from post
        end_template = "<!-- end of template -->"
        eti = post.find(end_template)
        if eti != -1:
            post = post[eti + len(end_template):]

        rendered_placeholder = (
            "\n\n{::nomarkdown}\n"
            "<div id=\"recipeSections\">\n  <!-- Recipe sections will be rendered here by JS -->\n</div>\n"
            "{:/}\n\n"
        )

        new_index = pre + rendered_placeholder + post
        INDEX_PATH.write_text(new_index, encoding="utf-8")

    if missing:
        print("WARNINGS:")
        for m in missing:
            print("-", m)

    print(f"Parsed {len(parsed)} recipe blocks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
