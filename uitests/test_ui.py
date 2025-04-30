import pytest

base_url = "http://localhost:8000/"

@pytest.mark.asyncio
async def test_ui_create_user(page):
    await page.goto(base_url)
    await page.wait_for_selector("#createUser")
    await page.click("#createUser")
    await page.wait_for_timeout(500)
    output = await page.locator("#output").inner_text()
    assert "User created" in output

@pytest.mark.asyncio
async def test_ui_get_user(page):
    await page.goto(base_url)
    await page.wait_for_selector("#getUser")
    await page.click("#getUser")
    await page.wait_for_timeout(500)
    output = await page.locator("#output").inner_text()
    assert "oksana" in output

@pytest.mark.asyncio
async def test_ui_update_user(page):
    await page.goto(base_url)
    await page.wait_for_selector("#updateUser")
    await page.click("#updateUser")
    await page.wait_for_timeout(500)
    output = await page.locator("#output").inner_text()
    assert "Sunnyvale" in output

@pytest.mark.asyncio
async def test_ui_delete_user(page):
    await page.goto(base_url)
    await page.wait_for_selector("#deleteUser")
    await page.click("#deleteUser")
    await page.wait_for_timeout(500)
    output = await page.locator("#output").inner_text()
    assert "User deleted" in output