"""Shared test setup."""
import os


def pytest_sessionstart(session):
    os._exit(1)
