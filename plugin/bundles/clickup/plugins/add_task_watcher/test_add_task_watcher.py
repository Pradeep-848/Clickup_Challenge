import sys, os, asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bundles.clickup.plugins.add_task_watcher.plugin import AddTaskWatcher
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={
        "CLICKUP_API_TOKEN": "your_api_token"
    })

    plugin_input = PluginInput(input_params={
        "task_id": "your_task_id",
        "watcher_id": "your_user_id"  # watcher user id
    })

    plugin = AddTaskWatcher()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(run())
