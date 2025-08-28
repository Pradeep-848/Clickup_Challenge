import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

import asyncio
from bundles.clickup.plugins.get_task.plugin import GetTask
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={"CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"})
    plugin_input = PluginInput(input_params={
        "task_id": "86d02wz5p"   # use your existing task id
    })
    plugin = GetTask()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

asyncio.run(run())
