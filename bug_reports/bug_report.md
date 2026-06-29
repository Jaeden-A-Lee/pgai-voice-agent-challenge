# Bug Report — Pretty Good AI Voice Agent (Pivot Point Orthopedics Demo)

All test calls made to +1-805-439-8008 using an automated AI patient persona via Vapi.

---

**Bug:** Agent says two different names for the same provider in one call

**Severity:** Medium

**Call:** transcript-scenario_3_reschedule_clean.txt at 2:16, 
    also in transcript-scenario_4_cancel_appointment.txt at 0:56

**Details:** This happened the same way in two separate calls. When the
agent says "Doctor" before the provider's name, it comes out correctly
as "Dr. Bricker." But when it says the name by itself, with no
"Doctor" in front, it comes out garbled, like "Abricker" or "Averker."
I checked both call recordings to confirm this wasn't just a
transcription mistake — the agent's actual voice says it differently
both ways. Not sure if this is the voice mispronouncing the name or the
system pulling a different name internally, but it happens consistently
enough that it's worth a look. A patient could get confused about their
doctor's actual name from this.