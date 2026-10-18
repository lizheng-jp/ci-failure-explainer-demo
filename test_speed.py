"""A timing test that is flaky on shared runners (see loadsim.py): it fails about half the time in CI."""
import time

from loadsim import runner_pause
from pricing import total


def test_total_is_fast_for_large_carts():
    start = time.perf_counter()
    runner_pause()
    total([1.0] * 10_000)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.5, f"pricing 10,000 items took {elapsed:.2f}s, budget 0.5s"
