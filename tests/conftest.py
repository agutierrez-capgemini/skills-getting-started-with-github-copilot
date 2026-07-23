from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset mutable in-memory activity data between tests."""
    snapshot = deepcopy(activities)
    yield
    activities.clear()
    activities.update(snapshot)
