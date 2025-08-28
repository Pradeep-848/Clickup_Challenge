import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class DeleteTask(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        endpoint = f"/task/{task_id}"

        try:
            result = await client.request("DELETE", endpoint)
            # If request() throws, we’ll handle below
        except Exception as e:
            if "204" in str(e):  # treat 204 as success
                return PluginOutput(data={"deleted_task_id": task_id, "response": "Task deleted successfully"})
            raise e

        return PluginOutput(data={"deleted_task_id": task_id, "response": json.dumps(result)})