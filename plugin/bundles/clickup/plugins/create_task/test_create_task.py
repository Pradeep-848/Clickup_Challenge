import sys, os
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

# import asyncio
from bundles.clickup.plugins.create_task.plugin import CreateTask
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={"CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"})
    plugin_input = PluginInput(input_params={
        "list_id": "901610509518",
        "name": "Test Task",
        "description": "Created from plugin test"
    })
    plugin = CreateTask()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

asyncio.run(run())
