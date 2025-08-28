import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class CreateTask(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        # Extract token from credentials
        
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Extract inputs
        list_id = plugin_input.input_params["list_id"]
        name = plugin_input.input_params["name"]
        description = plugin_input.input_params.get("description", "")
        assignees = plugin_input.input_params.get("assignees")
        priority = plugin_input.input_params.get("priority")
        due_date = plugin_input.input_params.get("due_date")

        # Build request body
        body = {
            "name": name,
            "description": description
        }
        if assignees:
            try:
                body["assignees"] = json.loads(assignees)  # expects list of user IDs
            except json.JSONDecodeError:
                body["assignees"] = [assignees]  # fallback: single ID
        if priority:
            body["priority"] = int(priority)
        if due_date:
            body["due_date"] = due_date  # ClickUp expects epoch ms

        # Call ClickUp API
        endpoint = f"/list/{list_id}/task"
        result = await client.request("POST", endpoint, json=body)

        # Format output
        task_data = {
            "id": result["id"],
            "name": result["name"],
            "status": result["status"]["status"],
            "url": result["url"],
            "date_created": result["date_created"]
        }

        return PluginOutput(data={"task": json.dumps(task_data)})
