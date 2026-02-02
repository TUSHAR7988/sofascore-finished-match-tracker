

import httpx
from utils.state import get_cookies

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.sofascore.com/",
    "Origin": "https://www.sofascore.com",
}

async def fetch_json(url):
    cookies = get_cookies()

    async with httpx.AsyncClient(
        headers=DEFAULT_HEADERS,
        cookies=cookies,
        timeout=10
    ) as client:
        r = await client.get(url)
        r.raise_for_status()
        return r.json()
