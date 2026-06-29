# Bug Report — Pretty Good AI Voice Agent (Pivot Point Orthopedics Demo)

All test calls made to +1-805-439-8008 using an automated AI patient persona via Vapi.

---

**Bug:** Agent says two different names for the same provider in one call

**Severity:** Medium

**Call:** transcript-scenario_3_reschedule_clean.txt at 2:16

**Details:** While listing open reschedule times, the agent called the
provider "Averker." A few turns later, when confirming the final
rescheduled appointment, it correctly said "Dr. Bricker," which matches
the provider from the original booking in scenario 1. I checked the
actual audio recording to confirm this wasn't just a transcription
mistake — the agent really did say two different names. A patient
hearing this might not know who they're actually seeing, especially if
they try to look the doctor up afterward.