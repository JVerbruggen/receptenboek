from __future__ import annotations

import argparse
import html as html_mod
import json
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

from extract_hellofresh import extract_recipe_from_html


ROOT = Path(__file__).resolve().parents[1]
RECIPES_JSON_PATH = ROOT / "assets" / "recipes.json"


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _derive_url_slug(url: str) -> str:
    segment = re.sub(r"[?#].*$", "", url).rstrip("/").split("/")[-1]
    segment = re.sub(r"-[0-9a-f]{16,}$", "", segment, flags=re.IGNORECASE)
    return segment


def _fetch(url: str, *, timeout: float = 30.0, sleep_s: float = 0.25) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()

    if sleep_s:
        time.sleep(sleep_s)

    return data.decode("utf-8", errors="ignore")


_TAG_RE = re.compile(r"<[^>]+>")


def _strip_html(s: str) -> str:
    if not s:
        return ""
    s = _TAG_RE.sub(" ", s)
    s = html_mod.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _to_step_objects(step_strings: list[str]) -> list[dict[str, Any]]:
    steps: list[dict[str, Any]] = []
    for idx, raw in enumerate(step_strings, start=1):
        text = _strip_html(raw)
        if not text:
            continue
        steps.append({"title": f"{idx} Stap {idx}", "items": [text]})
    return steps


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="Fetch HelloFresh recipe pages and fill missing ingredients/steps in assets/recipes.json"
    )
    ap.add_argument("--recipes-json", default=str(RECIPES_JSON_PATH), help="Path to assets/recipes.json")
    ap.add_argument("--urls-file", default="", help="Text file with URLs (one per line)")
    ap.add_argument("urls", nargs="*", help="HelloFresh recipe URLs")
    args = ap.parse_args(argv)

    urls: list[str] = []
    if args.urls_file:
        urls.extend(
            [
                ln.strip()
                for ln in Path(args.urls_file).read_text(encoding="utf-8").splitlines()
                if ln.strip() and not ln.strip().startswith("#")
            ]
        )
    urls.extend([u.strip() for u in args.urls if u.strip()])

    if not urls:
        print("No URLs provided", file=sys.stderr)
        return 2

    recipes_path = Path(args.recipes_json)
    cards = _load_json(recipes_path)
    if not isinstance(cards, list):
        print("recipes.json must be a list", file=sys.stderr)
        return 2

    by_slug: dict[str, dict[str, Any]] = {
        str(r.get("slug") or "").strip(): r for r in cards if isinstance(r, dict) and str(r.get("slug") or "").strip()
    }

    # Known rename mapping (URL slug -> existing card slug)
    rename_map = {
        "roerbaknoedels-met-boerenworst": "bulgogi-stir-fry-met-noedels-en-varkensboerenworst",
        "pittige-roerbak-met-udonnoedels-en-gemarineerde-eieren": "pittige-udonnoedels-met-gemarineerde-eieren",
    }

    updated = 0
    for url in urls:
        html = _fetch(url)
        fallback_slug = _derive_url_slug(url)
        extracted = extract_recipe_from_html(html, fallback_slug=fallback_slug)

        extracted_slug = extracted.slug
        url_slug = fallback_slug

        target_slug = None
        if extracted_slug in by_slug:
            target_slug = extracted_slug
        elif url_slug in by_slug:
            target_slug = url_slug
        elif url_slug in rename_map and rename_map[url_slug] in by_slug:
            target_slug = rename_map[url_slug]

        if not target_slug:
            print(
                f"SKIP {url} -> extracted slug '{extracted_slug}', url slug '{url_slug}': no matching recipe in recipes.json",
                file=sys.stderr,
            )
            continue

        target = by_slug[target_slug]

        # Only fill missing details; do not overwrite existing rich content.
        if not (isinstance(target.get("ingredients"), list) and target.get("ingredients")):
            target["ingredients"] = extracted.ingredients
        if not (isinstance(target.get("steps"), list) and target.get("steps")):
            target["steps"] = _to_step_objects(extracted.steps)

        if url and not target.get("source"):
            target["source"] = url

        if extracted.time and not str(target.get("time") or "").strip():
            target["time"] = extracted.time

        updated += 1
        print(f"UPDATED {target_slug} from {url}")

    if updated:
        _save_json(recipes_path, cards)
    print(f"Done. Updated {updated} recipe(s).")
    return 0 if updated else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
