import sys, os, asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bundles.clickup.plugins.create_list.plugin import CreateList
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={
        "CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"
    })

    plugin_input = PluginInput(input_params={
        "space_id": "90164829568",   # 👈 use your IT space id here
        "name": "My New List in Space",
        "content": "Created directly under IT space"
    })

    plugin = CreateList()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

asyncio.run(run())
