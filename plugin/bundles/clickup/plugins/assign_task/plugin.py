import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class AssignTask(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        assignee_id = plugin_input.input_params["assignee_id"]  # user id from your team

        endpoint = f"/task/{task_id}"
        body = {
            "assignees": {
                "add": [assignee_id]
            }
        }

        result = await client.request("PUT", endpoint, json=body)

        task_data = {
            "id": result.get("id"),
            "name": result.get("name"),
            "assignees": [a.get("username") for a in result.get("assignees", [])],
            "url": result.get("url")
        }

        return PluginOutput(data={"task": json.dumps(task_data)})
