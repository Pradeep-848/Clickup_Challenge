import sys, os, asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bundles.clickup.plugins.delete_task_comment.plugin import DeleteTaskComment
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={
        "CLICKUP_API_TOKEN": "pk_xxx"  # replace with your real API token
    })

    plugin_input = PluginInput(input_params={
        "comment_id": "90160131150125"   # replace with a real comment ID
    })

    plugin = DeleteTaskComment()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(run())
