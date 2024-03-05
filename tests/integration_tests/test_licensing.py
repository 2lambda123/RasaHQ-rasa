import os
import signal
import time
from pathlib import Path
from typing import Callable

import pytest
from pytest import MonkeyPatch
from _pytest.pytester import RunResult, Pytester

from rasa.utils.licensing import LICENSE_ENV_VAR


# licenses used in these tests
# they all expire on 26.01.2034
LICENSE_STUDIO = os.getenv("INTEGRATION_TESTS_STUDIO_LICENSE")
LICENSE_PRO = os.getenv("INTEGRATION_TESTS_PRO_LICENSE")
LICENSE_PRO_ALL_FEATURES = os.getenv("RASA_PRO_LICENSE")


@pytest.fixture
def audiocodes_credentials(tmp_path: Path) -> Path:
    """Fixture to create audiocodes credentials."""
    credentials = tmp_path / "credentials.yml"
    with credentials.open("w") as handle:
        handle.write(
            """
audiocodes:
  token: my-token
"""
        )

    yield credentials


def test_missing_license(
    monkeypatch: MonkeyPatch, run_in_simple_project: Callable[..., RunResult]
):
    monkeypatch.setenv(LICENSE_ENV_VAR, "")
    result = run_in_simple_project("--help")

    assert result.ret == 1
    assert (
        "Please set the environmental variable `RASA_PRO_LICENSE` to "
        "a valid license string."
    ) in str(result.stderr)


def test_missing_license_scope(
    monkeypatch: MonkeyPatch, run_in_simple_project: Callable[..., RunResult]
):
    monkeypatch.setenv(LICENSE_ENV_VAR, LICENSE_STUDIO)
    result = run_in_simple_project("--help")

    assert result.ret == 1
    assert (
        "Failed to validate Rasa Pro license which was read from environmental "
        "variable `RASA_PRO_LICENSE`. Please ensure `RASA_PRO_LICENSE` is set "
        "to a valid license string."
    ) in str(result.stderr)


def test_license_scope_ok(
    monkeypatch: MonkeyPatch,
    run_in_simple_project: Callable[..., RunResult],
):
    monkeypatch.setenv(LICENSE_ENV_VAR, LICENSE_PRO)
    result = run_in_simple_project("--help")

    assert result.ret == 0


def test_license_scope_missing_voice_scope(
    monkeypatch: MonkeyPatch,
    audiocodes_credentials: Path,
    run_in_simple_project: Callable[..., RunResult],
):
    monkeypatch.setenv(LICENSE_ENV_VAR, LICENSE_PRO)

    # first, train a model
    result = run_in_simple_project("train")
    assert result.ret == 0

    # then run
    result = run_in_simple_project("run", "--credentials", str(audiocodes_credentials))

    assert result.ret == 1
    assert (
        "The product scope of your issued license does not "
        "include rasa:pro:plus rasa:voice"
    ) in str(result.stderr)


def test_license_scope_voice_scope_ok(
    monkeypatch: MonkeyPatch,
    audiocodes_credentials,
    run_in_simple_project: Callable[..., RunResult],
    pytester: Pytester,
):
    monkeypatch.setenv(LICENSE_ENV_VAR, LICENSE_PRO_ALL_FEATURES)
    # first, train a model
    result = run_in_simple_project("train")
    assert result.ret == 0

    # then run; can't use run_in_simple_project() because
    # we need to communicate()
    popen = pytester.popen(
        # setting stdin to an empty bytes string prevents pytester
        # to close it; which is problematic below when we want to call
        # communicate()
        ["rasa", "run", "--credentials", str(audiocodes_credentials)],
        stdin=b"",
    )

    # sleep some time to let the time for the server to start
    time.sleep(10)
    # send CTR-C to the process
    popen.send_signal(signal.SIGINT)

    # read stderr mostly
    _, errs_bytes = popen.communicate()
    errs = errs_bytes.decode()

    # check that the voice channel is loaded
    assert (
        "Validating current Rasa Pro license scope which must include "
        "the 'rasa:voice' scope to use the voice channel."
    ) in errs
    # check that the license scope is validated
    assert "/webhooks/audiocodes/" in errs
    # check that the server started
    assert "Rasa server is up and running." in errs