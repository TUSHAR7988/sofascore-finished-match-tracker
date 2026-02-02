
from playwright.async_api import async_playwright
# from utils.proxy_loader import load_proxies, pick_proxy

async def start_browser():
    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled",
            "--blink-settings=imagesEnabled=false",
        ],
    )

    return playwright, browser

    # proxies = load_proxies()
    # proxy = pick_proxy(proxies)

    # launch_args = {
    #     "headless": True,
    #     "args": [
    #         "--no-sandbox",
    #         "--disable-gpu",
    #         "--disable-dev-shm-usage",
    #         "--disable-blink-features=AutomationControlled",
    #         "--blink-settings=imagesEnabled=false",
    #     ],
    # }

    # if proxy:
    #     launch_args["proxy"] = {
    #         "server": proxy
    #     }
    #     print("[PROXY] Using proxy:", proxy)

    # browser = await playwright.chromium.launch(**launch_args)

    # return playwright, browser

async def create_context(browser):
    context = await browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        ),
        locale="en-US",
        timezone_id="UTC",
        java_script_enabled=True,
    )

    await context.add_init_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
    )

    return context

async def get_cookies(context):
    cookies = await context.cookies()
    return {c["name"]: c["value"] for c in cookies}


async def browser_fetch_json(context, url):
    page = await context.new_page()
    try:
        # Load page without waiting for full network idle
        await page.goto(
            "https://www.sofascore.com/football",
            wait_until="domcontentloaded",
            timeout=30000
        )

        # Small human-like delay
        await page.wait_for_timeout(1500)

        # Convert API URL to relative path
        relative_url = url.replace("https://api.sofascore.com", "")

        data = await page.evaluate(
            """async (relativeUrl) => {
                const res = await fetch(relativeUrl, {
                    credentials: "include"
                });
                if (!res.ok) throw new Error("HTTP " + res.status);
                return await res.json();
            }""",
            relative_url,
        )

        return data
    finally:
        await page.close()


