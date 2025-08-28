import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class CreateList(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Extract inputs
        name = plugin_input.input_params["name"]
        space_id = plugin_input.input_params.get("space_id")
        folder_id = plugin_input.input_params.get("folder_id")  # optional

        # Optional fields
        content = plugin_input.input_params.get("content")
        due_date = plugin_input.input_params.get("due_date")
        priority = plugin_input.input_params.get("priority")

        # Body
        body = {"name": name}
        if content:
            body["content"] = content
        if due_date:
            body["due_date"] = due_date
        if priority:
            body["priority"] = priority

        # Endpoint: prefer folder_id if given, otherwise space_id
        if folder_id:
            endpoint = f"/folder/{folder_id}/list"
        elif space_id:
            endpoint = f"/space/{space_id}/list"
        else:
            raise Exception("Either folder_id or space_id must be provided")

        result = await client.request("POST", endpoint, json=body)

        list_data = {
            "id": result["id"],
            "name": result["name"],
            "url": result.get("url"),
            "space_id": result["space"]["id"],
            "folder_id": result["folder"]["id"] if "folder" in result else None
        }

        return PluginOutput(data={"list": json.dumps(list_data)})
