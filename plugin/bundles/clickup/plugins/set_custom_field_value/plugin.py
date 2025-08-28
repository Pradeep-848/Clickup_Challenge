import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class SetCustomFieldValue(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        field_id = plugin_input.input_params["field_id"]   # custom field ID
        value = plugin_input.input_params["value"]

        endpoint = f"/task/{task_id}/field/{field_id}"

        body = { "value": value }

        result = await client.request("POST", endpoint, json=body)

        field_data = {
            "task_id": task_id,
            "field_id": field_id,
            "updated_value": value,
            "response": result
        }

        return PluginOutput(data={"custom_field": json.dumps(field_data)})
