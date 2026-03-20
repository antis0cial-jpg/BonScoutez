import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Serve the file
        import os
        path = os.path.abspath("BonScout.html")
        await page.goto(f"file://{path}")

        # Click Demo Data
        await page.click("text=DEMO DATEN")
        await asyncio.sleep(1)

        # Verify Total Spend
        total_spend = await page.inner_text(".kpi:has-text('Gesamtausgaben') .v")
        print(f"Total Spend: {total_spend}")

        # Open History
        await page.click("text=BON-HISTORIE")
        await asyncio.sleep(0.5)

        # Check if history is visible
        history_visible = await page.is_visible("#historySection")
        print(f"History Visible: {history_visible}")

        # Hover over a history item
        await page.hover(".history-item:first-child")
        await asyncio.sleep(0.5)

        await page.screenshot(path="verification_history.png", full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
