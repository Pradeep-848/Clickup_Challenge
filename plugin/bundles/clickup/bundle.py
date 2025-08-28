from bundle_dependency import *
from aiohttp import ClientSession
from config import CONFIG

class YourBundle(BundleHandler):
    async def verify(self, credentials: BundleCredentials):
        api_key: str = credentials.credentials.get("CLICKUP_API_TOKEN")
        
        # Implement your verification logic here
        # Example:
        url = "https://api.example.com/verify"
        headers = {"Authorization": f"Bearer {api_key}"}
        
        async with ClientSession() as session:
            async with session.get(url=url, headers=headers, proxy=CONFIG.PROXY) as response:
                if response.status != 200:
                    raise_credentials_validation_error(await response.text())
