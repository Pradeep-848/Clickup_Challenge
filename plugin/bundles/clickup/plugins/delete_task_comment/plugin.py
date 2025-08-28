import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class DeleteTaskComment(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        # Get API token
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Inputs
        comment_id = plugin_input.input_params["comment_id"]

        # Endpoint
        endpoint = f"/comment/{comment_id}"

        # Perform delete
        result = await client.request("DELETE", endpoint)

        # Return response
        return PluginOutput(data={
            "deleted_comment_id": comment_id,
            "response": "Comment deleted successfully"
        })
