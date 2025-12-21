import os
import aiohttp
import asyncio
import logging
import sys

from bring_api import Bring

from dotenv import load_dotenv


# Load credentials from a local .env file (if present)
load_dotenv()

BRING_ACCOUNT = os.getenv("BRING_ACCOUNT", "")
BRING_PASSWORD = os.getenv("BRING_PASSWORD", "")

async def main():
    if not BRING_ACCOUNT or not BRING_PASSWORD:
        raise SystemExit(
            "Missing BRING_ACCOUNT/BRING_PASSWORD. Put them in synctobring/.env or set them in your environment."
        )
    async with aiohttp.ClientSession() as session:
        bring = Bring(session, BRING_ACCOUNT, BRING_PASSWORD)

        await bring.login()

        lists = (await bring.load_lists()).lists
        print(lists)

asyncio.run(main())