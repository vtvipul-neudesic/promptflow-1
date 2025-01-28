from promptflow import tool
import requests
import json
import os


@tool
def oai_search_tool(is_env_setup_successful: bool, user_prompt: str, max_tokens: int) -> dict:
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
