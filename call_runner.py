"""
call_runner.py

Triggers a single outbound Vapi call using our published assistant
(Pivot Point Orthopedics patient persona), overriding the system prompt
per call with a scenario-specific goal.
"""

import os
import requests
from dotenv import load_dotenv

from assistant_config import ASSISTANT_ID, build_system_prompt, ASSISTANT_MODEL_CONFIG

load_dotenv()

VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_PHONE_NUMBER_ID = os.getenv("VAPI_PHONE_NUMBER_ID")
TARGET_PHONE_NUMBER = os.getenv("TARGET_PHONE_NUMBER")

VAPI_CALL_URL = "https://api.vapi.ai/call"


def trigger_call(scenario_goal: str) -> dict:
    """
    Triggers one outbound call to the target test number, using our
    published assistant with a system prompt overridden for this
    specific scenario goal.

    Returns the parsed JSON response from Vapi (includes the call ID,
    which we'll need later to fetch the transcript/recording).
    """
    system_prompt = build_system_prompt(scenario_goal)

    payload = {
        "assistantId": ASSISTANT_ID,
        "phoneNumberId": VAPI_PHONE_NUMBER_ID,
        "customer": {
            "number": TARGET_PHONE_NUMBER
        },
        "assistantOverrides": {
            "model": {
                "provider": ASSISTANT_MODEL_CONFIG["provider"],
                "model": ASSISTANT_MODEL_CONFIG["model"],
                "temperature": ASSISTANT_MODEL_CONFIG["temperature"],
                "maxTokens": ASSISTANT_MODEL_CONFIG["max_tokens"],
                "messages": [
                    {
                        "role": "system",
                        "content": system_prompt
                    }
                ]
            }
        }
    }

    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(VAPI_CALL_URL, json=payload, headers=headers)

    if response.status_code not in (200, 201):
        raise RuntimeError(
            f"Vapi call request failed ({response.status_code}): {response.text}"
        )

    return response.json()


if __name__ == "__main__":
    # Quick manual test: trigger one simple call before wiring up the
    # full scenario loop in main.py.
    scenario_1_goal = (
        "Call to schedule a general appointment as a new patient at this "
        "practice. You twisted your ankle playing basketball recently and "
        "want to be seen soon. If asked, confirm you are a new patient."
    )

    result = trigger_call(scenario_1_goal)
    print("Call triggered successfully.")
    print("Call ID:", result.get("id"))
    print("Full response:", result)