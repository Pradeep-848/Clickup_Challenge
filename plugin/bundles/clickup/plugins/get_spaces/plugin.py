import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class GetSpaces(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        team_id = plugin_input.input_params["team_id"]

        endpoint = f"/team/{team_id}/space"

        result = await client.request("GET", endpoint)

        spaces_data = []
        for space in result.get("spaces", []):
            spaces_data.append({
                "id": space.get("id"),
                "name": space.get("name"),
                "private": space.get("private"),
                "multiple_assignees": space.get("multiple_assignees"),
                "archived": space.get("archived"),
                "statuses": [s.get("status") for s in space.get("statuses", [])]
            })

        return PluginOutput(data={"spaces": json.dumps(spaces_data)})
