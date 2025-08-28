import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class CreateChecklist(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        checklist_name = plugin_input.input_params["name"]

        endpoint = f"/task/{task_id}/checklist"
        body = {"name": checklist_name}

        result = await client.request("POST", endpoint, json=body)

        checklist_data = {
            "id": result.get("id"),
            "name": result.get("name"),
            "task_id": task_id
        }

        return PluginOutput(data={"checklist": json.dumps(checklist_data)})
