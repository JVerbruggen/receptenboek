"""Fix truncated step titles in recipes.json by generating logical titles from step content."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RECIPES_JSON_PATH = ROOT / "assets" / "recipes.json"


def extract_action_from_steps(items: list[str]) -> str:
    """Extract a logical action/title from the step items."""
    if not items:
        return "Voorbereiden"

    first_item = items[0].strip()

    # Common patterns to extract meaningful titles
    patterns = [
        (r"^(Verwarm de oven|Verwarm) voor op", "Oven voorverwarmen"),
        (r"^Breng ruim water.*aan de kook", "Water koken"),
        (r"^Kook ruim water", "Water koken"),
        (r"^V erhit", "Roomboter verhitten"),  # Fix typo
        (r"^Verhit.*roomboter.*pan", "Roomboter verhitten"),
        (r"^Verhit.*olijfolie.*pan", "Olijfolie verhitten"),
        (r"^Verhit.*zonnebloemolie", "Olie verhitten"),
        (r"^Verhit.*sesamolie", "Sesamolie verhitten"),
        (r"^Verhit een koekenpan", "Pan verhitten"),
        (r"^Verhit een scheutje", "Olie verhitten"),
        (r"^Verhit.*el", "Olie verhitten"),
        (r"^Snijd de ui in halve ringen", "Ui snijden en bakken"),
        (r"^Snijd de (ui|knoflook|paprika|wortel)", lambda m: f"{m.group(1).capitalize()} snijden"),
        (r"^Bak de (ui|knoflook)", "Ui bakken"),
        (r"^Bak de ([a-z]+)", lambda m: f"{m.group(1).capitalize()} bakken"),
        (r"^Voeg.*roomboter.*toe", "Roomboter toevoegen"),
        (r"^Voeg, vlak voor serveren", "Afwerken en serveren"),
        (r"^Voeg de (rode splitlinzen|zwarte-bonenpasta|kookroom)", "Ingrediënten toevoegen"),
        (r"^Voeg.*toe", "Ingrediënten toevoegen"),
        (r"^Blus.*af", "Afblussen"),
        (r"^Haal het deksel van de pan", "Pan afwerken"),
        (r"^Verdeel.*over de (borden|kommen)", "Serveren"),
        (r"^Serveer", "Serveren"),
        (r"^Meng", "Mengen"),
        (r"^Snijd", "Snijden"),
        (r"^Snipper", "Voorbereiden"),
        (r"^Pers", "Voorbereiden"),
        (r"^Rasp", "Voorbereiden"),
        (r"^Bereid de bouillon", "Bouillon bereiden"),
        (r"^Kook.*bouillonblokje", "Bouillon maken"),
        (r"^Kook.*de rijst.*afgedekt", "Rijst koken"),
        (r"^Kook de (rijst|noedels|pasta)", lambda m: f"{m.group(1).capitalize()} koken"),
        (r"^Dep.*droog", "Voorbereiden"),
        (r"^Roer\s+de\s+spinazie\s+door", "Spinazie toevoegen"),
        (r"^Voeg\s+de\s+paneer\s+met\s+dressing", "Paneer toevoegen"),
        (r"^Bak\s+de\s+naan\s+\d+\s*-\s*\d+\s+minuten", "Naan bakken"),
        (r"^Roer", "Roeren"),
        (r"^Stamp de", "Puree maken"),
    ]

    for pattern, replacement in patterns:
        match = re.search(pattern, first_item, re.IGNORECASE)
        if match:
            if callable(replacement):
                return replacement(match)
            return replacement

    # Fallback: take first 3-5 words
    words = first_item.split()[:5]
    title = " ".join(words)
    # Remove trailing punctuation
    title = re.sub(r'[,.:;]+$', '', title)
    return title


def is_truncated_title(title: str) -> bool:
    """Check if a title appears to be truncated or awkward."""
    title_lower = title.lower()
    # Remove step number prefix
    clean_title = re.sub(r'^\d+\s+', '', title)

    truncation_patterns = [
        r'\baan de\s*$',
        r'\bin een\s*$',
        r'\bin de\s*$',
        r'\bvoor op\s*$',
        r'\bper persoon\s*$',
        r'\bop middel\s*$',
        r'\bmet een\s*$',
        r'\bover de\s*$',
        r'\bop het\s*$',
        r'\bin het\s*$',
        r'\btoe aan\s*$',
        r'\bmet de\s*$',
        r'\bsch eutje\s*$',  # typo in original
        r'\bin halve\s*$',
        r'\bde bouillon\s*$',
        r'\bde rijst\s*$',
        r'\bde aardappelen\s*$',
        r'\bde pasta\s*$',
        r'\bde noedels\s*$',
        r'\broomboter,\s*ketjap\s*$',
        r'\bde aardappel en wortel\s*$',
        r'\bde wortelpuree en broccoli\s*$',
        r'\bafgedekt,\s*$',
        r'\bde risotto over de\s*$',
        r'^verhit\s+\d+/\d+\s+el\s+(olijfolie|zonnebloemolie)\s+per\s*$',
        r'^verhit\s+een\s+(scheutje|klontje|sch\s+eutje)\s+(olijfolie|roomboter|zonnebloemolie)\s+in\s*$',
        r'^verhit\s+\d+/\d+\s+van\s+de\s+(olijfolie|zonnebloemolie)\s*$',
        r'^verhit\s+de\s+(sesamolie|olijfolie|overige)\s+(en\s+de|olijfolie\s+in|in)\s*$',
        r'^verhit\s+een\s+koekenpan\s+zonder\s+olie\s*$',
        r'^v\s+erhit\s+',  # typo "V erhit"
        r'^voeg\s+\d+/\d+\s+van\s+de\s+bouillon\s*$',
        r'^voeg\s+de\s+(rode\s+splitlinzen|kookroom)\s+toe,?\s*$',
        r'^voeg\s+de\s+zwarte-bonenpasta,\s+de\s+bosui\s*$',
        r'^voeg\s+de\s+\w+\s+en\s+per\s*$',
        r'^voeg,\s+vlak\s+voor\s+serveren,\s+de\s*$',
        r'^voeg\s+de\s+paneer\s+met\s+dressing\s*$',
        r'^roer\s+de\s+spinazie\s+door\s+de\s*$',
        r'^bak\s+de\s+naan\s+\d+\s*-\s*$',
        r'^haal\s+het\s+deksel\s+van\s+de\s*$',
    ]

    return any(re.search(pattern, clean_title, re.IGNORECASE) for pattern in truncation_patterns)


def fix_recipe_titles(recipe: dict[str, Any]) -> dict[str, Any]:
    """Fix truncated step titles in a recipe."""
    steps = recipe.get("steps", [])
    if not isinstance(steps, list):
        return recipe

    fixed_count = 0
    for idx, step in enumerate(steps, 1):
        if not isinstance(step, dict):
            continue

        title = step.get("title", "")
        items = step.get("items", [])

        if not isinstance(items, list):
            continue

        if is_truncated_title(title):
            # Generate a better title
            new_action = extract_action_from_steps(items)
            new_title = f"{idx} {new_action}"
            step["title"] = new_title
            fixed_count += 1
            print(f"  Fixed: '{title}' -> '{new_title}'")

    return recipe


def main() -> int:
    """Fix all truncated step titles in recipes.json."""
    data = json.loads(RECIPES_JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("assets/recipes.json must be a JSON list")

    total_fixed = 0
    for recipe in data:
        if not isinstance(recipe, dict):
            continue

        recipe_title = recipe.get("title", "Unknown")
        print(f"\nProcessing: {recipe_title}")

        original = json.dumps(recipe)
        fixed_recipe = fix_recipe_titles(recipe)
        modified = json.dumps(fixed_recipe)

        if original != modified:
            total_fixed += 1

    # Save the fixed data
    RECIPES_JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"\n\nTotal recipes with fixes: {total_fixed}")
    print(f"Updated: {RECIPES_JSON_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
