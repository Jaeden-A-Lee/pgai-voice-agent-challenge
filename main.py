
"""
main.py

Runs through the full list of test scenarios (scenarios/scenario_list.py),
triggering one real outbound call per scenario via call_runner, waiting
for each to complete, and saving the transcript + recording via
fetch_results before moving to the next scenario.

Run with: python main.py
Optionally run a single scenario by index: python main.py 3
"""

import sys

from call_runner import trigger_call
from fetch_results import fetch_and_save_results
from scenarios.scenario_list import SCENARIOS


def run_scenario(scenario: dict):
    name = scenario["name"]
    goal = scenario["goal"]

    print(f"\n=== Running {name} ===")
    result = trigger_call(goal)
    call_id = result["id"]
    print(f"Call triggered. Call ID: {call_id}")

    fetch_and_save_results(call_id, name)
    print(f"=== Finished {name} ===\n")


def run_all():
    for scenario in SCENARIOS:
        run_scenario(scenario)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run a single scenario by its 1-based index, e.g. `python main.py 3`
        index = int(sys.argv[1]) - 1
        if 0 <= index < len(SCENARIOS):
            run_scenario(SCENARIOS[index])
        else:
            print(f"Invalid scenario index. Choose 1-{len(SCENARIOS)}.")
    else:
        run_all()