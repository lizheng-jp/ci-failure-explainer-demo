"""Simulates a shared CI runner under load, so the timing test in test_speed.py is flaky on purpose.

About half of all CI runs (and reruns) are "slow", independently of any code change; local runs never are.
"""
import os
import time


def runner_pause() -> None:
    run = int(os.environ.get("GITHUB_RUN_ID", "1")) + int(os.environ.get("GITHUB_RUN_ATTEMPT", "0"))
    time.sleep(0.6 if run % 2 == 0 else 0.0)
