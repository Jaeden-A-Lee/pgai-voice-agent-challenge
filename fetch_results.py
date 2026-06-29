"""
fetch_results.py

Fetches the transcript and recording for a completed Vapi call, and
saves both locally (transcripts/ and recordings/), using the call's
Vapi-assigned ID.
"""

import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_CALL_BASE_URL = "https://api.vapi.ai/call"

# Statuses that mean the call is fully finished and data should be ready
TERMINAL_STATUSES = {"ended"}

# Statuses that mean the call failed outright and will never reach "ended"
# with usable data — fail fast instead of waiting out the full timeout
FAILURE_STATUSES = {"failed"}


def get_call_details(call_id: str) -> dict:
    """Fetches the current state of a call from Vapi."""
    headers = {"Authorization": f"Bearer {VAPI_API_KEY}"}
    response = requests.get(f"{VAPI_CALL_BASE_URL}/{call_id}", headers=headers)

    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to fetch call {call_id} ({response.status_code}): {response.text}"
        )

    return response.json()


def wait_for_call_completion(call_id: str, poll_interval: int = 10, timeout: int = 480) -> dict:
    """
    Polls Vapi until the call status is 'ended', or until timeout (seconds).
    Returns the final call details.
    """
    elapsed = 0
    while elapsed < timeout:
        details = get_call_details(call_id)
        status = details.get("status")
        print(f"  Call status: {status} (waited {elapsed}s)")

        if status in TERMINAL_STATUSES:
            return details

        if status in FAILURE_STATUSES:
            raise RuntimeError(f"Call {call_id} failed with status: {status}")

        time.sleep(poll_interval)
        elapsed += poll_interval

    raise TimeoutError(f"Call {call_id} did not finish within {timeout} seconds.")


def save_transcript(call_id: str, scenario_name: str, details: dict) -> str:
    """
    Builds a clearly-labeled transcript from the structured messages
    array (rather than Vapi's default flat transcript string, which
    labels turns ambiguously as "AI"/"User"), and saves it to
    transcripts/<scenario_name>.txt
    """
    artifact = details.get("artifact", {})
    messages = artifact.get("messages", [])

    label_map = {
        "assistant": "Vapi",
        "bot": "Vapi",
        "user": "Pretty Good AI",
        "system": "System Prompt",
    }

    lines = []
    for msg in messages:
        role = msg.get("role", "unknown")
        text = msg.get("message", "")

        # Skip the system prompt itself — not part of the spoken conversation
        if role == "system":
            continue

        label = label_map.get(role, role)
        lines.append(f"{label}: {text}")

    if lines:
        transcript = "\n".join(lines)
    else:
        # Fallback to the flat transcript string if structured messages are missing
        transcript = artifact.get("transcript", "No transcript available.")

    path = f"transcripts/{scenario_name}.txt"

    with open(path, "w") as f:
        f.write(f"Call ID: {call_id}\n")
        f.write(f"Scenario: {scenario_name}\n")
        f.write("=" * 50 + "\n\n")
        f.write(transcript)

    print(f"  Saved transcript to {path}")
    return path


def save_recording(call_id: str, scenario_name: str, details: dict) -> str:
    """Downloads the recording audio file to recordings/<scenario_name>.mp3"""
    artifact = details.get("artifact", {})
    recording = artifact.get("recording", {})
    recording_url = recording.get("stereoUrl") or recording.get("mono", {}).get("combinedUrl")

    if not recording_url:
        print("  No recording URL found in call details.")
        return None

    audio_response = requests.get(recording_url)
    path = f"recordings/{scenario_name}.mp3"

    with open(path, "wb") as f:
        f.write(audio_response.content)

    print(f"  Saved recording to {path}")
    return path


def fetch_and_save_results(call_id: str, scenario_name: str) -> dict:
    """
    Full pipeline: wait for the call to finish, then save transcript
    and recording locally under the given scenario_name.
    """
    print(f"Waiting for call {call_id} to complete...")
    details = wait_for_call_completion(call_id)

    save_transcript(call_id, scenario_name, details)
    save_recording(call_id, scenario_name, details)

    return details


if __name__ == "__main__":
    # Manual test: paste in a real call_id from a call you've already
    # triggered via call_runner.py, to test fetching independently.
    test_call_id = "PASTE_CALL_ID_HERE"
    test_scenario_name = "scenario_1_new_patient_scheduling"

    fetch_and_save_results(test_call_id, test_scenario_name)