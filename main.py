

import asyncio
from core.browser import start_browser, create_context, get_cookies
from poller.finished_detector import poll_finished_matches
from utils.state import set_cookies

async def main():
    playwright, browser = await start_browser()
    context = await create_context(browser)

    print("Browser + context initialized")

    # ✅ NEW PART — session bootstrap
    # page = await context.new_page()
    # await page.goto("https://www.sofascore.com", timeout=30000)
    # await page.wait_for_timeout(3000)

    # cookies = await get_cookies(context)
    # set_cookies(cookies)

    # await page.close()
    # print("Session cookies acquired")

    try:
        await poll_finished_matches(context)
    finally:
        print("Shutting down...")
        await context.close()
        await browser.close()
        await playwright.stop()

if __name__ == "__main__":
    asyncio.run(main())
