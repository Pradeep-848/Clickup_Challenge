import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class CreateSpace(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Required params
        team_id = plugin_input.input_params["team_id"]
        name = plugin_input.input_params["name"]

        # Optional settings
        multiple_assignees = plugin_input.input_params.get("multiple_assignees", True)
        features = plugin_input.input_params.get("features", {})

        endpoint = f"/team/{team_id}/space"

        body = {
            "name": name,
            "multiple_assignees": multiple_assignees,
            "features": features or {
                "due_dates": {"enabled": True, "start_date": True, "remap_due_dates": True, "remap_closed_due_date": False},
                "sprints": {"enabled": True},
                "time_tracking": {"enabled": True},
                "tags": {"enabled": True},
                "points": {"enabled": True},
                "custom_items": {"enabled": True},
                "priorities": {"enabled": True, "priorities": []},
                "check_unresolved": {"enabled": True, "subtasks": True, "checklists": True, "comments": True}
            }
        }

        result = await client.request("POST", endpoint, json=body)

        space_data = {
            "id": result.get("id"),
            "name": result.get("name"),
            "private": result.get("private"),
            "multiple_assignees": result.get("multiple_assignees"),
            "archived": result.get("archived")
        }

        return PluginOutput(data={"space": json.dumps(space_data)})
