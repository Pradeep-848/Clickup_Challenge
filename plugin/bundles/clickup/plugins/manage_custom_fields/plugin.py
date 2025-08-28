from bundle_dependency import *
from shared.api_client import ClickUpAPIClient

class CreateTask(PluginHandler):
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        api_token = credentials.credentials.get("pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV")
        client = ClickUpAPIClient(api_token)
        
        list_id = plugin_input.input_params["list_id"]
        name = plugin_input.input_params["name"]
        
        response = await client.request(
            "POST",
            f"list/{list_id}/task",
            data={"name": name}
        )
        
        return PluginOutput(data={"task": response})