# Architecture

## How it works

The system uses Vapi as a managed voice orchestration layer to place
outbound calls to Pretty Good AI's demo line. When a scenario runs,
`call_runner.py` sends a POST request to Vapi's `/call` endpoint with
three things: the target phone number, a reference to a pre-published
Vapi assistant (which handles voice/model configuration), and an
`assistantOverrides` payload that injects a scenario-specific system
prompt for that call. This prompt tells the AI patient persona who it
is (Jiggy Johnathon, DOB 07/04/2000) and what its goal is for this
specific call. Vapi then places the real phone call, runs the full
STT→LLM→TTS pipeline internally, and records both sides of the
conversation. Once the call ends, `fetch_results.py` polls Vapi's
API until the call status is "ended," then downloads the transcript
(from `artifact.messages`) and recording (from
`artifact.recording.stereoUrl`) and saves both locally.

## Key design decisions

**Vapi for voice orchestration instead of building a raw pipeline.**
The alternative was wiring together Twilio for telephony, Deepgram
for real-time STT, OpenAI for the LLM, and ElevenLabs for TTS over
a live WebSocket — handling turn-taking, latency stacking, and
barge-in detection manually. Since voice interaction quality was the
primary evaluation criterion, I chose to use Vapi's managed layer
instead, which handles the real-time audio pipeline and turn-taking
reliably out of the box. This freed up time to focus on what
actually differentiates the submission: realistic persona design,
scenario coverage, and bug-finding quality.

**One parameterized persona prompt instead of 12 separate ones.**
The patient's identity (name, DOB) is fixed across all calls since
we're calling from one number and the system uses caller ID to
recognize returning patients. Only the scenario goal changes per
call. Separating fixed identity from variable intent means a single
prompt template, built in `assistant_config.py`, drives all 12
scenarios — easier to maintain, easier to iterate on, and cleaner
to reason about when something goes wrong.

**`assistantOverrides` for per-call system prompt injection.**
Rather than creating 12 separate Vapi assistants or patching the
dashboard assistant before each call, we use Vapi's
`assistantOverrides` field to inject the scenario-specific system
prompt at call time while keeping the voice and model config
centralized in the published assistant. This means the entire
behavioral configuration for any given call is visible in code,
not split between a dashboard and a script.

**Polling instead of webhooks for call completion.**
Fetching results after a call requires knowing when the call has
ended. A webhook-based approach would require running a public
server to receive Vapi's completion event. Instead, `fetch_results.py`
polls the `/call/{id}` endpoint every 10 seconds until status is
"ended" or a failure status is detected. For a single-developer
test tool making 12 calls, polling is simpler, requires no
infrastructure, and works reliably within the call durations we
observed (all calls ended within 3 minutes).