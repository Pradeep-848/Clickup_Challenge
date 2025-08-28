import json
from bundle_dependency import *
from bundles.clickup.shared.api_client import ClickUpClient

class SearchTasks(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        # Get API token
        api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
        client = ClickUpClient(api_token)

        # Extract required inputs
        team_id = plugin_input.input_params["team_id"]
        query = plugin_input.input_params["query"]

        # Extract optional filters
        list_id = plugin_input.input_params.get("list_id")
        status = plugin_input.input_params.get("status")
        assignee = plugin_input.input_params.get("assignee")

        # Build endpoint with query params
        endpoint = f"/team/{team_id}/task?query={query}&include_closed=true"

        if list_id:
            endpoint += f"&list_ids[]={list_id}"
        if status:
            endpoint += f"&statuses[]={status}"
        if assignee:
            endpoint += f"&assignees[]={assignee}"

        # Call API
        result = await client.request("GET", endpoint)

        # Simplify results
        tasks_data = []
        for task in result.get("tasks", []):
            tasks_data.append({
                "id": task["id"],
                "name": task["name"],
                "status": task["status"]["status"],
                "url": task["url"],
                "list_id": task["list"]["id"]
            })

        return PluginOutput(data={"tasks": json.dumps(tasks_data)})


# import json
# from bundle_dependency import *
# from bundles.clickup.shared.api_client import ClickUpClient

# class SearchTasks(PluginHandler):
#     async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
#         # Get API token
#         api_token = credentials.credentials.get("CLICKUP_API_TOKEN")
#         client = ClickUpClient(api_token)

#         # Extract inputs
#         team_id = plugin_input.input_params["team_id"]
#         query = plugin_input.input_params["query"]

#         # Build endpoint
#         endpoint = f"/team/{team_id}/task?query={query}&include_closed=true"

#         # Call API
#         result = await client.request("GET", endpoint)

#         # Simplify results
#         tasks_data = []
#         for task in result.get("tasks", []):
#             tasks_data.append({
#                 "id": task["id"],
#                 "name": task["name"],
#                 "status": task["status"]["status"],
#                 "url": task["url"],
#                 "list_id": task["list"]["id"]
#             })

#         return PluginOutput(data={"tasks": json.dumps(tasks_data)})
