import requests
from dotenv import load_dotenv
import os
import json
import streamlit as st

load_dotenv()


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "76be4ad9-16e5-448a-8521-cebe2706f02d"
FLOW_ID = "37aa588b-bc3c-4581-9d60-2b13aa4f3b86"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "MovieMate" # The endpoint name of the flow



def run_flow(message: str,) -> dict:
    
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


def main():
    frontend()
    
    st.set_page_config(page_title="MovieMate - Your Movie Companion", layout="wide")
    st.title ("Chat Interface")

    message = st. text_area ("Message", placeholder="Ask something...")
    
    if st. button ("Run Flow"):
        if not message.strip():
            st.error ("Please enter a message")
            return
        
        try:
            with st. spinner ("Running flow..."):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"] ["message"] ["text"]
            st. markdown (response)
        except Exception as e:
            st. error (str(e))


if __name__ == "__main__":
    main()

