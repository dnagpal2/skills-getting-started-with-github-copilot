import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities before and after each test."""
    original = copy.deepcopy(app_module.activities)
    app_module.activities = copy.deepcopy(original)
    yield
    app_module.activities = copy.deepcopy(original)


@pytest.fixture
def client():
    return TestClient(app_module.app)
