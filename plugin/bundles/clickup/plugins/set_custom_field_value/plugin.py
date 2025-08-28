import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class SetCustomFieldValue(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        task_id = plugin_input.input_params["task_id"]
        field_id = plugin_input.input_params["field_id"]
        value = plugin_input.input_params["value"]

        # ✅ Update custom field value
        endpoint = f"/task/{task_id}/field/{field_id}"
        body = {"value": value}
        await client.request("POST", endpoint, json=body)

        # ✅ Now fetch task to confirm
        task_endpoint = f"/task/{task_id}"
        task_data = await client.request("GET", task_endpoint)

        confirmed = None
        confirmed_label = None
        for f in task_data.get("custom_fields", []):
            if f.get("id") == field_id:
                confirmed = f
                # resolve label if dropdown
                if f.get("type") == "drop_down":
                    options = f.get("type_config", {}).get("options", [])
                    for opt in options:
                        if str(opt.get("id")) == str(value):
                            confirmed_label = opt.get("name")
                            break
                break

        result_data = {
            "task_id": task_id,
            "field_id": field_id,
            "updated_value": value,
            "confirmed_label": confirmed_label,
            "confirmed_value": confirmed
        }

        return PluginOutput(data={"custom_field": json.dumps(result_data)})
