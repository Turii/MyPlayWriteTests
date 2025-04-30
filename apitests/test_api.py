import pytest

base_url = "http://localhost:8000/users"

@pytest.mark.asyncio
async def test_create_user(page, user_data):
    response = await page.request.post(base_url, data=user_data)
    assert response.status == 201

@pytest.mark.asyncio
async def test_get_user(page):
    response = await page.request.get(f"{base_url}/1")
    assert response.status == 200

@pytest.mark.asyncio
async def test_update_user(page):
    update_data = {"location": "Sunnyvale", "age": 31}
    response = await page.request.put(f"{base_url}/1", data=update_data)
    assert response.status == 200

@pytest.mark.asyncio
async def test_delete_user(page):
    response = await page.request.delete(f"{base_url}/1")
    assert response.status == 200
    await page.close()