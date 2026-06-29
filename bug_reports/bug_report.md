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


**Bug:** Agent processes a controlled substance refill with no extra verification or caution

**Severity:** High

**Call:** transcript-scenario_5_medication_refill.txt at 1:00

**Details:** I called asking for a refill on oxycodone for an ankle
injury. The agent handled it exactly like any other refill request —
asked which medication, how many days left, callback number, and
pharmacy info, then said it documented the request for the team to
review. It never mentioned anything about needing provider approval,
never flagged it as a controlled substance, and never verified the
prescription against anything on file. The tone never changed either.
For a medication like this, I'd expect at least some extra step or
language acknowledging it's different from a routine refill.


**Bug:** Several rough turn-taking and audio moments in one call

**Severity:** Low

**Call:** transcript-scenario_5_medication_refill.txt at 0:17 (DOB), 
    at 1:16 (phone number), at 1:44 (agent jumped in fast), 
    at 1:49 (vapi pharmacy interruption), at 2:50 (mumbled/pause)

**Details:** A few different spots in this call had noticeable audio
or pacing issues. The line asking for date of birth came through
quieter than the rest of the call. Reading my phone number back
didn't sound as smooth as the rest of its speech. Right after I
finished explaining I had no new symptoms, the agent jumped in fast
enough that it felt slightly rushed. A bit later, the agent paused
mid-sentence asking for the pharmacy name, long enough that I started
responding before it continued with the rest of its question. Near
the end, while documenting the refill request, part of its sentence
came through mumbled or dropped, like the mic didn't pick it up
clearly. None of these broke the conversation, but together they made
this particular call feel less polished than the others.