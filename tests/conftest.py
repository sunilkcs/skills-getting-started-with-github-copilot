import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def activity_store(monkeypatch):
    fresh_activities = copy.deepcopy(app_module.activities)
    monkeypatch.setattr(app_module, "activities", fresh_activities)
    return fresh_activities


@pytest.fixture
def client(activity_store):
    with TestClient(app_module.app) as test_client:
        yield test_client