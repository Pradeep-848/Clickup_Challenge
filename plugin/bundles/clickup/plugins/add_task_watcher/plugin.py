import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class AddTaskWatcher(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        watcher_id = plugin_input.input_params["watcher_id"]

        endpoint = f"/task/{task_id}/watcher/{watcher_id}"

        result = await client.request("POST", endpoint)

        watcher_data = {
            "task_id": task_id,
            "watcher_id": watcher_id,
            "status": "added"
        }

        return PluginOutput(data={"watcher": json.dumps(watcher_data)})
