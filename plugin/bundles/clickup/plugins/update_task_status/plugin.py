import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class UpdateTaskStatus(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Required params
        task_id = plugin_input.input_params["task_id"]
        new_status = plugin_input.input_params["status"]   # e.g. "✅ resolved"

        endpoint = f"/task/{task_id}"

        body = {
            "status": new_status
        }

        result = await client.request("PUT", endpoint, json=body)

        task_data = {
            "id": result.get("id"),
            "name": result.get("name"),
            "status": result.get("status", {}).get("status"),
            "url": result.get("url"),
            "date_updated": result.get("date_updated")
        }

        return PluginOutput(data={"task": json.dumps(task_data)})
