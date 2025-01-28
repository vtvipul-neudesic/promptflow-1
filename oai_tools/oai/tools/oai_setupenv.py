import os
from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def oai_setupenv_tool(
    api_key: str, endpoint: str, deployment_name: str, setupenv: bool
) -> str:
    """
    This tool sets up the environment variables for the OAI tools
    """
    if not setupenv:
        return False
    os.environ["API_KEY"] = api_key
    os.environ["ENDPOINT"] = endpoint
    os.environ["DEPLOYMENT_NAME"] = deployment_name
    return True
