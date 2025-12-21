from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RECIPES_JSON_PATH = ROOT / "assets" / "recipes.json"


RECIPE_KEY_ORDER = [
    "title",
    "slug",
    "time",
    "tags",
    "image",
    "source",
    "servings",
    "servings_text",
    "ingredients",
    "steps",
]

INGREDIENT_KEY_ORDER = ["name", "amount"]
STEP_KEY_ORDER = ["title", "items"]


_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")


def _split_into_sentences(text: str) -> list[str]:
    t = str(text or "").strip()
    if not t:
        return []
    parts = [p.strip() for p in _SENTENCE_SPLIT_RE.split(t) if p.strip()]
    return parts or [t]


def _short_title_from_text(text: str) -> str:
    # Best-effort: derive a short descriptive title from the first sentence.
    first = (text or "").strip()
    if not first:
        return "Stap"
    first = re.sub(r"^[\-\s]+", "", first)
    first = re.sub(r"\s+", " ", first)
    # Take up to 5 words.
    words = first.split(" ")
    short = " ".join(words[:5])
    # Trim trailing punctuation
    short = short.rstrip(" .!?:;")
    return short or "Stap"


def _normalize_step_title(existing_title: str, idx: int, first_item_text: str) -> str:
    raw = str(existing_title or "").strip()
    raw = re.sub(r"\s+", " ", raw)

    # Remove any leading numbering like "1" or "1." or "Stap 1" etc.
    raw_no_num = re.sub(r"^\d+\s*([.)-])?\s*", "", raw)
    raw_no_num = re.sub(r"^stap\s*\d+\s*([:)\-])?\s*", "", raw_no_num, flags=re.IGNORECASE)
    raw_no_num = raw_no_num.strip()

    # If the remaining title is empty or generic, derive from first item.
    if not raw_no_num or raw_no_num.lower() in {"stap", ""}:
        raw_no_num = _short_title_from_text(first_item_text)

    return f"{idx} {raw_no_num}".strip()


def reorder_dict(d: dict[str, Any], order: list[str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for k in order:
        if k in d:
            out[k] = d[k]

    # Preserve any extra keys (stable), but keep them at the end.
    for k, v in d.items():
        if k not in out:
            out[k] = v

    return out


def _drop_empty_top_level(recipe: dict[str, Any]) -> dict[str, Any]:
    # Keep the Aubergine-example style: don't include null/empty optional fields.
    # Note: we intentionally do NOT drop empty ingredient amounts, since "" can be meaningful there.
    for key in ("time", "source", "servings", "servings_text"):
        if key not in recipe:
            continue
        v = recipe.get(key)
        if v is None:
            recipe.pop(key, None)
            continue
        if isinstance(v, str) and not v.strip():
            recipe.pop(key, None)
            continue
    if isinstance(recipe.get("tags"), list) and len(recipe.get("tags") or []) == 0:
        recipe.pop("tags", None)
    return recipe


def _coerce_steps_to_objects(steps: list[Any]) -> list[dict[str, Any]]:
    # Aubergine example uses step objects: { title, items }
    out: list[dict[str, Any]] = []
    idx = 1
    for step in steps:
        if isinstance(step, dict):
            s = reorder_dict(step, STEP_KEY_ORDER)
            title = str(s.get("title") or "").strip()
            items = s.get("items")
            if isinstance(items, str) and items.strip():
                items = [items.strip()]
            elif not isinstance(items, list):
                items = []

            # Split each item into sentence-level list items.
            split_items: list[str] = []
            for x in items:
                split_items.extend(_split_into_sentences(str(x)))
            split_items = [p for p in (s.strip() for s in split_items) if p]

            first_text = split_items[0] if split_items else ""
            normalized_title = _normalize_step_title(title, idx, first_text)
            out.append({"title": normalized_title, "items": split_items})
            idx += 1
            continue

        if isinstance(step, str):
            text = step.strip()
            if not text:
                continue

            split_items = _split_into_sentences(text)
            first_text = split_items[0] if split_items else text
            normalized_title = _normalize_step_title("", idx, first_text)
            out.append({"title": normalized_title, "items": split_items})
            idx += 1
            continue

    return out


def normalize_recipe(r: Any) -> Any:
    if not isinstance(r, dict):
        return r

    out = reorder_dict(r, RECIPE_KEY_ORDER)

    # Normalize nested structures
    ingredients = out.get("ingredients")
    if isinstance(ingredients, list):
        normalized_ingredients: list[Any] = []
        for ing in ingredients:
            if isinstance(ing, dict):
                normalized_ingredients.append(reorder_dict(ing, INGREDIENT_KEY_ORDER))
            else:
                normalized_ingredients.append(ing)
        out["ingredients"] = normalized_ingredients

    # If ingredients is present but empty, drop it (to match the example style)
    if isinstance(out.get("ingredients"), list) and len(out.get("ingredients") or []) == 0:
        out.pop("ingredients", None)

    steps = out.get("steps")
    if isinstance(steps, list):
        out["steps"] = _coerce_steps_to_objects(steps)

    if isinstance(out.get("steps"), list) and len(out.get("steps") or []) == 0:
        out.pop("steps", None)

    out = _drop_empty_top_level(out)

    return out


def main() -> int:
    data = json.loads(RECIPES_JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("assets/recipes.json must be a JSON list")

    normalized = [normalize_recipe(r) for r in data]

    RECIPES_JSON_PATH.write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Formatted {len(normalized)} recipes -> {RECIPES_JSON_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
