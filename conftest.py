import pytest
import pytest_asyncio
import subprocess
import time
import signal
import json
from playwright.async_api import async_playwright

@pytest.fixture(scope="session", autouse=True)
def flask_app():
    process = subprocess.Popen(["python", "api/app.py"])
    time.sleep(1.5)
    yield
    process.send_signal(signal.SIGINT)
    process.wait()

@pytest_asyncio.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()

@pytest.fixture
def user_data():
    with open("apitests/data/user_data.json") as f:
        return json.load(f)