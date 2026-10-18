# ci-failure-explainer demo

A minimal repository showing [ci-failure-explainer](https://github.com/lizheng-jp/ci-failure-explainer):
when the `CI` workflow fails on a pull request, `.github/workflows/explain-ci-failure.yml` comments on the PR
with the likely cause and the files to look at. See the closed and open pull requests for example comments.

## Example pull requests

Each pull request below breaks CI in a different way on purpose. The comments were posted by the action itself.

| PR | What was broken | The action's diagnosis | Files it pointed to | Screenshot |
|---|---|---|---|---|
| [#1](https://github.com/lizheng-jp/ci-failure-explainer-demo/pull/1) | discount applied the wrong way round | code defect, high confidence | `pricing.py` | [png](docs/screenshots/pr-1.png) |
| [#2](https://github.com/lizheng-jp/ci-failure-explainer-demo/pull/2) | unused import fails the `ruff` lint job | lint / format / type check | `pricing.py` | [png](docs/screenshots/pr-2.png) |
| [#3](https://github.com/lizheng-jp/ci-failure-explainer-demo/pull/3) | `pytest==99.0.0` does not exist | dependency or environment change | `requirements.txt` | [png](docs/screenshots/pr-3.png) |
| [#4](https://github.com/lizheng-jp/ci-failure-explainer-demo/pull/4) | README-only change; the timing test in `test_speed.py` is flaky on purpose (see `loadsim.py`) | flaky test, likely not this change | `test_speed.py` | [png](docs/screenshots/pr-4.png) |
| [#5](https://github.com/lizheng-jp/ci-failure-explainer-demo/pull/5) | a new `conftest.py` exits silently, so the log shows no error at all | the test setup itself | `conftest.py` | [png](docs/screenshots/pr-5.png) |

In #5 the log holds nothing but `exit code 1`; the diagnosis comes from the pull request's file list. Each
comment cost about US$0.008.
