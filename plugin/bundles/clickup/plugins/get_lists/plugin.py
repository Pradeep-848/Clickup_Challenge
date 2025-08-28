import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class GetLists(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Required params
        space_id = plugin_input.input_params["space_id"]

        # Optional folder_id (lists can belong to folders or directly under space)
        folder_id = plugin_input.input_params.get("folder_id")

        if folder_id:
            endpoint = f"/folder/{folder_id}/list"
        else:
            endpoint = f"/space/{space_id}/list"

        result = await client.request("GET", endpoint)

        # Simplify response
        lists_data = []
        for lst in result.get("lists", []):
            lists_data.append({
                "id": lst.get("id"),
                "name": lst.get("name"),
                "orderindex": lst.get("orderindex"),
                "task_count": lst.get("task_count"),
                "archived": lst.get("archived"),
                "folder_id": lst.get("folder", {}).get("id"),
                "space_id": lst.get("space", {}).get("id"),
            })

        return PluginOutput(data={"lists": json.dumps(lists_data)})
