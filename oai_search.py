import requests
import json
import os
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(is_env_setup_successful: bool, user_prompt: str, max_tokens: int) -> dict:
    if not is_env_setup_successful:
        return False
    headers = {"Content-Type": "application/json", "api-key": os.getenv("API_KEY")}
    data = {"prompt": user_prompt, "max_tokens": max_tokens}
    response = requests.post(
        f"{os.getenv('ENDPOINT')}/openai/deployments/{os.getenv('DEPLOYMENT_NAME')}/completions?api-version=2022-12-01",
        headers=headers,
        data=json.dumps(data),
    )
    return response.json()
