import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class GetTimeEntries(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        endpoint = f"/task/{task_id}/time"

        result = await client.request("GET", endpoint)

        entries = []
        for e in result.get("data", []):
            entries.append({
                "id": e.get("id"),
                "description": e.get("description"),
                "duration": e.get("duration"),
                "start": e.get("start"),
                "end": e.get("end"),
                "user": e.get("user", {}).get("username")
            })

        return PluginOutput(data={"time_entries": json.dumps(entries)})
