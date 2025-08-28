import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

import asyncio
from bundles.clickup.plugins.search_tasks.plugin import SearchTasks
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={"CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"})
    plugin_input = PluginInput(input_params={
    "team_id": "90161193440",
    "query": "Task",
    "list_id": "901610509518",    # optional
    "status": "✅ resolved",      # optional
    "assignee": "224694395"       # optional
    })
    plugin = SearchTasks()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

asyncio.run(run())


# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

# import asyncio
# from bundles.clickup.plugins.search_tasks.plugin import SearchTasks
# from bundle_dependency import PluginInput, BundleCredentials

# async def run():
#     credentials = BundleCredentials(credentials={"CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"})
#     plugin_input = PluginInput(input_params={
#         "team_id": "90161193440",
#         "query": "Test"
#     })
#     plugin = SearchTasks()
#     result = await plugin.execute(credentials, plugin_input)
#     print(result.data)

# asyncio.run(run())