import sys, os, asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bundles.clickup.plugins.update_task_status.plugin import UpdateTaskStatus
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={
        "CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"
    })

    plugin_input = PluginInput(input_params={
        "task_id": "86d00cg06",             # your real task ID
        "status": "\u2705 resolved",            # new status
        "name": "Refund Issue Investigation"  # also update name
    })

    plugin = UpdateTaskStatus()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(run())


# import sys, os, asyncio
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

# from bundles.clickup.plugins.update_task_status.plugin import UpdateTaskStatus
# from bundle_dependency import PluginInput, BundleCredentials

# async def run():
#     credentials = BundleCredentials(credentials={
#         "CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"
#     })

#     plugin_input = PluginInput(input_params={
#         "task_id": "86d00cg06",      # replace with your real task ID
#         "status": "✅ resolved" 
#     })

#     plugin = UpdateTaskStatus()
#     result = await plugin.execute(credentials, plugin_input)
#     print(result.data)

# if __name__ == "__main__":
#     asyncio.run(run())
