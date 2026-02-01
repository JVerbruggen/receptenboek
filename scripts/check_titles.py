"""Check for any remaining problematic step titles."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES_JSON_PATH = ROOT / "assets" / "recipes.json"

data = json.loads(RECIPES_JSON_PATH.read_text(encoding="utf-8"))

suspicious = []
for recipe in data:
    if not isinstance(recipe, dict):
        continue
    recipe_title = recipe.get("title", "Unknown")
    steps = recipe.get("steps", [])
    for step in steps:
        if not isinstance(step, dict):
            continue
        title = step.get("title", "")
        # Check for very short titles or titles ending with prepositions/articles
        if (len(title) < 25 or
            title.endswith(('in', 'de', 'een', 'aan', 'toe', 'per', 'met', 'op', 'voor', 'over', 'het'))):
            suspicious.append(f"{recipe_title}: {title}")

if suspicious:
    print(f"Found {len(suspicious)} potentially problematic titles:\n")
    for item in suspicious[:30]:
        print(item)
else:
    print("No suspicious titles found!")
