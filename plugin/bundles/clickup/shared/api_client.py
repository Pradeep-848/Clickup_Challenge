import aiohttp
from config import CONFIG

class ClickUpClient:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = "https://api.clickup.com/api/v2"

    async def request(self, method: str, endpoint: str, **kwargs):
        headers = {
            "Authorization": self.api_token,
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}{endpoint}"

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, proxy=CONFIG.PROXY, **kwargs) as response:
                if response.status in (200, 201):
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"ClickUp API Error {response.status}: {error_text}")
