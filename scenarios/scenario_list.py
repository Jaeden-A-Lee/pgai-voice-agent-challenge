"""
scenario_list.py

The 12 test scenarios used to drive outbound calls against Pretty Good
AI's demo voice agent. Each scenario has a unique name (used for file
naming in transcripts/ and recordings/) and a goal (the instruction
given to our Vapi patient persona for that specific call).

Designed to cover the required scenario categories from the challenge
brief, plus targeted edge cases based on real findings from manual
test calls (see bug_reports/ and our own earlier notes).
"""

SCENARIOS = [
    {
        "name": "scenario_1_new_patient_scheduling",
        "goal": (
            "Call to schedule a general appointment as a new patient at this "
            "practice. You twisted your ankle playing basketball recently and "
            "want to be seen soon. If asked, confirm you are a new patient."
        ),
    },
    {
        "name": "scenario_2_urgent_same_day",
        "goal": (
            "You are an existing patient calling back. You are having sudden, "
            "sharp pain in your ankle today that feels worse than before, and "
            "you want to be seen today if at all possible. Express urgency "
            "clearly and ask specifically if same-day or urgent care "
            "availability exists, rather than just asking for the soonest "
            "appointment in general."
        ),
    },
    {
        "name": "scenario_3_reschedule_clean",
        "goal": (
            "You are an existing patient with an upcoming appointment "
            "(scheduled during a previous call) that you need to move. "
            "Clearly state you'd like to reschedule, and when asked, "
            "say you'd prefer a day later in the same week if possible. "
            "Be clear and specific, not vague, about what you want."
        ),
    },
    {
        "name": "scenario_4_cancel_appointment",
        "goal": (
            "You are an existing patient who needs to cancel your upcoming "
            "appointment entirely, not reschedule it. State clearly that you "
            "want to cancel, and explain briefly that your schedule changed "
            "and you no longer need the visit right now."
        ),
    },
    {
        "name": "scenario_5_medication_refill",
        "goal": (
            "You are an existing patient calling to request a refill on a "
            "pain medication prescribed after your ankle injury. You're "
            "running low and want to make sure you don't run out."
        ),
    },
    {
        "name": "scenario_6_hours_question_cold",
        "goal": (
            "As soon as the call connects, before any other context, ask "
            "directly: 'What are your office hours?' Do not state a name, "
            "reason for calling, or any other intent first. Just ask the "
            "hours question immediately."
        ),
    },
    {
        "name": "scenario_7_insurance_question_obscure",
        "goal": (
            "Call and ask whether the practice accepts an uncommon or "
            "unusual insurance plan (make one up that sounds plausible "
            "but obscure, e.g. a small regional or out-of-state plan). "
            "See how the agent responds to a plan it may not recognize."
        ),
    },
    {
        "name": "scenario_8_closed_day_scheduling",
        "goal": (
            "Call to schedule an appointment and specifically ask to come "
            "in this Sunday. If told that's not available, ask directly "
            "why, and whether the office is closed that day."
        ),
    },
    {
        "name": "scenario_9_vague_reschedule",
        "goal": (
            "Call to reschedule an appointment, but be intentionally vague "
            "at first about which appointment you mean (say you're not "
            "sure if it was last week or next week). If the agent pushes "
            "back or asks clarifying questions, then provide clearer "
            "details and resolve it naturally."
        ),
    },
    {
        "name": "scenario_10_out_of_scope_request",
        "goal": (
            "Call and ask the agent to tell you what your recent X-ray or "
            "MRI results showed. This is a medical question outside what "
            "a scheduling agent should answer directly — see whether it "
            "escalates you to a human/provider or attempts to answer anyway."
        ),
    },
    {
        "name": "scenario_11_after_hours_callback",
        "goal": (
            "Call and explain that you have been trying to reach the "
            "office for a while and keep getting this automated system. "
            "Ask if there is any way to speak to a real person or get "
            "a callback from a human staff member. See how the agent "
            "handles a patient who explicitly wants human contact rather "
            "than continuing with the AI system."
        ),
    },
    {
        "name": "scenario_12_compound_unclear_intent",
        "goal": (
            "Call and open with an intentionally compound, somewhat "
            "unclear request: say something like 'I'm having some issues "
            "with my arm and I think I might need to come in, or maybe "
            "just get a refill, I'm not totally sure.' See how the agent "
            "disambiguates between multiple possible intents."
        ),
    },
]