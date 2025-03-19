from robocorp.tasks import task
import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from robocorp import browser as robocorp_browser

# This is optional, it is used to load the environment variables from the .env file
# Now environment variables are loaded from the env.json file (the Robocorp way)
# from dotenv import load_dotenv
# load_dotenv()


# This is used to install browsers for the Playwright
robocorp_browser.configure()


async def main():
    # Basic configuration
    config = BrowserConfig(headless=True, disable_security=True)
    browser = Browser(config=config)
    try:
        # video: https://preview.screen.studio/share/70xBqZyN
        llm = ChatOpenAI(model="gpt-4o")
        agent = Agent(
            browser=browser,
            # task="Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result",
            # task="Go to amazon.com. Dismiss address popup. Search for external hard drive, sort by best rating, and give me the price of the top three result and the link to the product.",
            task="Go to govtrack.us, search for bill 'IHS Workforce Parity Act of 2025' and give me the summary of the bill",
            llm=llm,
        )
        await agent.run()
    finally:
        await browser.close()


@task
def minimal_task():
    asyncio.run(main())
