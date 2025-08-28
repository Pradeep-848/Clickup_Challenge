import sys, os, asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bundles.clickup.plugins.set_custom_field_value.plugin import SetCustomFieldValue
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={
        "CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"
    })

    plugin_input = PluginInput(input_params={
    "task_id": "86d00cg06",  # your real task ID
    "field_id": "537cc5dc-2c11-4dea-a1f3-a14c62d7b349",  # Department
    "value": "4ca184b0-3875-4789-bf1c-19e3573ac2e3"      # option ID for 📢 Marketing
    })

    plugin = SetCustomFieldValue()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(run())
