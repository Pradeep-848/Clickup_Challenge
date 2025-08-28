import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class UpdateTask(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        # Get API token
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Extract inputs
        task_id = plugin_input.input_params["task_id"]
        name = plugin_input.input_params.get("name")
        description = plugin_input.input_params.get("description")
        status = plugin_input.input_params.get("status")
        priority = plugin_input.input_params.get("priority")
        due_date = plugin_input.input_params.get("due_date")

        # Build request body (only include fields that were passed)
        body = {}
        if name: body["name"] = name
        if description: body["description"] = description
        if status: body["status"] = status
        if priority: body["priority"] = int(priority)
        if due_date: body["due_date"] = due_date  # epoch ms

        # API call
        endpoint = f"/task/{task_id}"
        result = await client.request("PUT", endpoint, json=body)

        # Format response
        task_data = {
            "id": result["id"],
            "name": result["name"],
            "status": result["status"]["status"],
            "url": result["url"],
            "date_updated": result["date_updated"]
        }

        return PluginOutput(data={"task": json.dumps(task_data)})
