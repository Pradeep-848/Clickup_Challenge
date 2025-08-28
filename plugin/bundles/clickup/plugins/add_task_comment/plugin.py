import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class AddTaskComment(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        comment_text = plugin_input.input_params["comment_text"]

        endpoint = f"/task/{task_id}/comment"

        # ✅ Correct payload for ClickUp
        body = {
            "comment_text": comment_text,
            "notify_all": True
        }

        result = await client.request("POST", endpoint, json=body)

        comment_data = {
            "id": result.get("id"),
            "comment_text": result.get("comment_text"),
            "user": result.get("user", {}).get("username") if result.get("user") else None,
            "date": result.get("date"),
        }

        return PluginOutput(data={"comment": json.dumps(comment_data)})
