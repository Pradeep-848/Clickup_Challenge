import sys, os, asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bundles.clickup.plugins.add_task_watcher.plugin import AddTaskWatcher
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={
        "CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"
    })

    plugin_input = PluginInput(input_params={
        "task_id": "86d02wz5p",   # your real task id
        "user_id": 224694395      # watcher user id
    })

    plugin = AddTaskWatcher()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(run())
