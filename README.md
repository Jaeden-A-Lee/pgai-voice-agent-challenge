# PGAI Voice Agent Challenge

An automated outbound voice bot that calls Pretty Good AI's demo line
(+1-805-439-8008) and conducts realistic patient conversations across
12 test scenarios. Built for Pretty Good AI's AI Engineering Challenge.

## What it does

- Places real outbound calls using Vapi's voice infrastructure
- Simulates a patient persona (Jiggy Johnathon) across 12 distinct scenarios
- Records and transcribes every call automatically
- Covers required categories: scheduling, rescheduling, cancellation,
  medication refills, insurance questions, office hours, and edge cases

## Setup

### Prerequisites
- Python 3.9+
- A Vapi account with a provisioned phone number
- An OpenAI API key

### Installation

1. Clone the repo:
```bash
   git clone https://github.com/Jaeden-A-Lee/pgai-voice-agent-challenge.git
   cd pgai-voice-agent-challenge
```

2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and fill in your real values:
```bash
   cp .env.example .env
```

   Required variables:
   - `VAPI_API_KEY` — your Vapi private API key
   - `VAPI_PHONE_NUMBER_ID` — UUID of your Vapi phone number (not the number itself)
   - `OPENAI_API_KEY` — your OpenAI API key
   - `TARGET_PHONE_NUMBER` — the number to call (E.164 format)

5. Create a Vapi assistant in the dashboard with ElevenLabs voice (Roger,
   `eleven_turbo_v2_5`) and paste its ID into `assistant_config.py` as
   `ASSISTANT_ID`.

## Running

### Run a single scenario (recommended for testing)
```bash
python main.py 2
```
Replace `2` with any scenario number 1–12.

### Run all scenarios
```bash
python main.py
```

Results are saved automatically to `transcripts/` and `recordings/`.

## Project structure

```
pgai-voice-agent-challenge/
├── main.py                  # Scenario runner (single or full batch)
├── assistant_config.py      # Patient persona, voice/model config
├── call_runner.py           # Triggers outbound Vapi calls
├── fetch_results.py         # Polls for call completion, saves results
├── scenarios/
│   └── scenario_list.py     # All 12 scenario definitions
├── transcripts/             # Saved call transcripts (.txt)
├── recordings/              # Saved call recordings (.mp3)
├── bug_reports/
│   └── bug_report.md        # Documented issues found during testing
├── .env.example             # Environment variable template
└── requirements.txt         # Python dependencies
```

## Test phone number used
All calls placed from Vapi number: `+15138227358`