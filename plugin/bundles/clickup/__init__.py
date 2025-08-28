from bundle_dependency import *
from aiohttp import ClientSession
from config import CONFIG
from bundle_dependency import BundleHandler, BundleCredentials, raise_credentials_validation_error

class ClickUpBundle(BundleHandler):
    async def verify(self, credentials: BundleCredentials):
        headers = {"Authorization": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"}
        
        async with ClientSession() as session:
            async with session.get(
                "https://api.clickup.com/api/v2/team",
                headers=headers,
                proxy=CONFIG.PROXY
            ) as response:
                if response.status != 200:
                    raise_credentials_validation_error(await response.text())