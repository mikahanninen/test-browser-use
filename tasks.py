from robocorp.tasks import task
import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from robocorp import browser

# from dotenv import load_dotenv

# load_dotenv()
browser.configure()


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
