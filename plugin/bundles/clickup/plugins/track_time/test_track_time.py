import sys, os, asyncio, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

import time

from bundles.clickup.plugins.track_time.plugin import TrackTime
from bundle_dependency import PluginInput, BundleCredentials

async def run():
    credentials = BundleCredentials(credentials={
        "CLICKUP_API_TOKEN": "pk_224694395_67HX9N5GIA9E3JT9BZ2LWIPBRQ8P32DV"
    })

    now = int(time.time() * 1000)
    plugin_input = PluginInput(input_params={
    "task_id": "86d02wz5p",
    "start": now - 600000,  # 10 minutes ago
    "end": now,             # now
    "description": "Test tracking - 10min"
    })

    plugin = TrackTime()
    result = await plugin.execute(credentials, plugin_input)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(run())
