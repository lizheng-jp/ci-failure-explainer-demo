"""Simulates a shared CI runner under load, so the timing test in test_speed.py is flaky on purpose.

About half of all CI runs are "slow", independently of any code change; locally runs are never slow.
"""
import os
import time


def runner_pause() -> None:
    run_id = int(os.environ.get("GITHUB_RUN_ID", "1"))
    time.sleep(0.6 if run_id % 2 == 0 else 0.0)
