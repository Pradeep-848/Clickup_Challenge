import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class GetTask(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        # Get API token
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Extract task_id from input
        task_id = plugin_input.input_params["task_id"]

        # API call
        endpoint = f"/task/{task_id}"
        result = await client.request("GET", endpoint)

        # Format response
        task_data = {
            "id": result["id"],
            "name": result["name"],
            "status": result["status"]["status"],
            "url": result["url"],
            "list_id": result["list"]["id"],
            "date_created": result["date_created"],
            "date_updated": result["date_updated"],
        }

        return PluginOutput(data={"task": json.dumps(task_data)})
