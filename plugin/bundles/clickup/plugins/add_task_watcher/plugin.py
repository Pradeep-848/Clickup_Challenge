import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class AddTaskWatcher(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        user_id = plugin_input.input_params["user_id"]  # Watcher User ID

        endpoint = f"/task/{task_id}"

        body = {
            "watchers": [user_id]
        }

        result = await client.request("PUT", endpoint, json=body)

        task = {
            "id": result.get("id"),
            "name": result.get("name"),
            "watchers": [u.get("username") for u in result.get("watchers", [])],
            "url": result.get("url")
        }

        return PluginOutput(data={"task": json.dumps(task)})
