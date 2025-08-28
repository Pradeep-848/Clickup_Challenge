# A:\Clickup_Challenge\bundle_dependency.py
from typing import Any, Dict, Optional
from dataclasses import dataclass

@dataclass
class BundleCredentials:
    credentials: Dict[str, Any]

@dataclass  
class PluginInput:
    input_params: Dict[str, Any]

@dataclass
class PluginOutput:
    data: Dict[str, Any]

class BundleHandler:
    async def verify(self, credentials: BundleCredentials):
        pass

class PluginHandler:
    async def execute(self, credentials: BundleCredentials, plugin_input: PluginInput) -> PluginOutput:
        pass

def raise_credentials_validation_error(message: str):
    raise ValueError(f"Credentials validation error: {message}")

def raise_provider_api_error(message: str):
    raise ValueError(f"API error: {message}")