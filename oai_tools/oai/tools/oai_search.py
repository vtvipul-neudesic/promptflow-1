from promptflow import tool
import requests
import json
from promptflow.connections import CustomConnection

@tool
def oai_search_tool(connection: CustomConnection, user_prompt: str, max_tokens: int) -> dict:
    endpoint = connection.configs.get("oai_endpoint")
    deployment_name = connection.configs.get("deployment_name")
    api_key = connection.secrets.get("oai_api_key")
    headers = {"Content-Type": "application/json", "api-key": api_key}
    data = {"prompt": user_prompt, "max_tokens": max_tokens}
    response = requests.post(
        f"{endpoint}/openai/deployments/{deployment_name}/completions?api-version=2022-12-01",
        headers=headers,
        data=json.dumps(data),
    )
    return response.json()
