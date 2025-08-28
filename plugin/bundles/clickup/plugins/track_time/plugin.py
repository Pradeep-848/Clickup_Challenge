import time
import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class TrackTime(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]

        # Start time (default = now if not provided)
        start = plugin_input.input_params.get("start", int(time.time() * 1000)-7200000)

        # Either use duration or end
        duration = plugin_input.input_params.get("duration")
        end = plugin_input.input_params.get("end")

        if not end and duration:
            end = start + duration

        description = plugin_input.input_params.get("description", "Tracked via API")

        endpoint = f"/task/{task_id}/time"

        body = {
            "start": start,
            "end": end,
            "description": description
        }

        result = await client.request("POST", endpoint, json=body)

        time_entry = {
            "id": result.get("id"),
            "task_id": result.get("task", {}).get("id"),
            "description": result.get("description"),
            "duration": result.get("duration"),
            "start": result.get("start"),
            "end": result.get("end")
        }

        return PluginOutput(data={"time_entry": json.dumps(time_entry)})
