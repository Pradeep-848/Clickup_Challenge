import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class CreateChecklist(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        name = plugin_input.input_params.get("name", "New Checklist")

        endpoint = f"/task/{task_id}/checklist"
        body = {"name": name}

        result = await client.request("POST", endpoint, json=body)
        checklist_data = result.get("checklist", {})
        checklist = {
            "id": checklist_data.get("id"),
            "name": checklist_data.get("name"),
            "task_id": (task_id)
        }

        return PluginOutput(data={"checklist": json.dumps(checklist)})
