import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class GetCustomFields(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        list_id = plugin_input.input_params["list_id"]

        endpoint = f"/list/{list_id}/field"

        result = await client.request("GET", endpoint)

        fields_data = []
        for field in result.get("fields", []):
            fields_data.append({
                "id": field.get("id"),
                "name": field.get("name"),
                "type": field.get("type_config", {}).get("type"),
                "required": field.get("required"),
                "options": field.get("type_config", {}).get("options", [])
            })

        return PluginOutput(data={"custom_fields": json.dumps(fields_data)})
