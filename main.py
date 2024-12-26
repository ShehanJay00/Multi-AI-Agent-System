import requests


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "76be4ad9-16e5-448a-8521-cebe2706f02d"
FLOW_ID = "37aa588b-bc3c-4581-9d60-2b13aa4f3b86"
APPLICATION_TOKEN = "<YOUR_APPLICATION_TOKEN>"
ENDPOINT = "MovieMate" # The endpoint name of the flow



def run_flow(message: str,) -> dict:
    
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

