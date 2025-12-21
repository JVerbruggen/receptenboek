import os
import aiohttp
import asyncio
import logging

from bring_api import Bring, BringTemplate, TemplateType
from bring_api.types import Ingredient

from dotenv import load_dotenv

# using api https://github.com/miaucl/bring-api/blob/main/bring_api/bring.py

# Load credentials from a local .env file (if present)
load_dotenv()

public_base_url = "https://jverbruggen.github.io"
githubpage_base_url = f"{public_base_url}/receptenboek"

BRING_ACCOUNT = os.getenv("BRING_ACCOUNT", "")
BRING_PASSWORD = os.getenv("BRING_PASSWORD", "")

MY_TAG = "jurjensrecepten"

recepten_json = "../assets/recipes.json"

def load_recipes_into_bring_templates():
    import json

    with open(recepten_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    templates = []
    for r in data:
        if not isinstance(r, dict):
            continue
        title = r.get("title") or "Onbekend recept"
        slug = r.get("slug") or ""
        url = f"{githubpage_base_url}/#{slug}" if slug else ""
        ingredients = r.get("ingredients") or []
        template_items: list[Ingredient] = []
        for ing in ingredients:
            if not isinstance(ing, dict):
                continue
            name = ing.get("name") or ""
            amount = ing.get("amount")
            if not name:
                continue
            template_items.append(
                Ingredient(
                    itemId=name,
                    stock=False,
                    spec=str(amount) if amount else None,
                )
            )
        template = BringTemplate(
            name=title,
            items=template_items,
            ingredients=template_items,
            tags=[MY_TAG],
            linkOutUrl=url,
            template_type=TemplateType.RECIPE,
        )
        templates.append(template)
    return templates

async def create_templates_in_bring(bring: Bring, templates: list[BringTemplate]):
    for template in templates:
        print(f"Creating template: {template.name}")
        await bring.create_template(template)
        print(f"Created template: {template.name}")

async def delete_existing_with_tag(bring: Bring, tag: str):
    existing_inspirations = await bring.get_inspirations(filter=tag)
    print(f"Found {len(existing_inspirations.entries)} existing templates with tag {tag}")
    for insp in existing_inspirations.entries:

        uuid = insp.content.uuid

        print(f"Deleting existing template: {uuid}")

        await bring.delete_template(uuid)
        print(f"Deleted existing template: {uuid}")

async def main():
    if not BRING_ACCOUNT or not BRING_PASSWORD:
        raise SystemExit(
            "Missing BRING_ACCOUNT/BRING_PASSWORD. Put them in synctobring/.env or set them in your environment."
        )
    async with aiohttp.ClientSession() as session:
        bring = Bring(session, BRING_ACCOUNT, BRING_PASSWORD)
        print("Logging in to Bring...")

        await bring.login()
        print("Logged in to Bring account.")

        # lists = (await bring.load_lists()).lists
        # print(lists)

        await delete_existing_with_tag(bring, MY_TAG)

        templates = load_recipes_into_bring_templates()
        await create_templates_in_bring(bring, templates)

        # await bring.create_template(
        #     template=BringTemplate(
        #         name="Test template from synctobring",
        #         items=[
        #             Ingredient(itemId="Test item 1", stock=False, spec="2"),
        #             Ingredient(itemId="Test item 2", stock=False, spec="1 kg"),
        #         ],
        #         ingredients=[
        #             Ingredient(itemId="Test item 1", stock=False, spec="2"),
        #             Ingredient(itemId="Test item 2", stock=False, spec="1 kg"),
        #         ],
        #         tags=[MY_TAG],
        #         imageUrl="https://jverbruggen.github.io/receptenboek/assets/images/zoete-aardappelstoof-met-zure-room-en-jalapeno.jpg",
        #     ),
        #     template_type=TemplateType.RECIPE,
        # )


if __name__ == "__main__":
    asyncio.run(main())