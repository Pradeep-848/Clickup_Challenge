import sys, os, asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bundles.clickup.plugins.create_checklist.plugin import CreateChecklist
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={
        "CLICKUP_API_TOKEN": "your_api_token"
    })

    plugin_input = PluginInput(input_params={
        "task_id": "your_task_id",
        "name": "QA Checklist"
    })

    plugin = CreateChecklist()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(run())
