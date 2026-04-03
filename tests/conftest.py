"""Pytest configuration and fixtures for the FastAPI application tests."""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI application."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to known state before and after each test."""
    initial_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Team practices and matches for soccer enthusiasts",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 22,
            "participants": ["liam@mergington.edu", "noah@mergington.edu"]
        },
        "Basketball Training": {
            "description": "Develop basketball skills, teamwork, and fitness",
            "schedule": "Mondays, Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 18,
            "participants": ["ava@mergington.edu", "lucas@mergington.edu"]
        },
        "Yoga Club": {
            "description": "Mindfulness, flexibility, and wellness through yoga",
            "schedule": "Fridays, 3:00 PM - 4:00 PM",
            "max_participants": 25,
            "participants": ["sophia@mergington.edu", "ethan@mergington.edu"]
        },
        "Art Studio": {
            "description": "Painting, sketching, and mixed media art sessions",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["mia@mergington.edu", "isabella@mergington.edu"]
        },
        "Drama Club": {
            "description": "Acting workshops and stage performance preparation",
            "schedule": "Thursdays, 3:30 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["jack@mergington.edu", "amelia@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop arguments, public speaking, and critical thinking",
            "schedule": "Mondays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["oliver@mergington.edu", "emma@mergington.edu"]
        },
        "Science Club": {
            "description": "Hands-on experiments and science exploration",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["mason@mergington.edu", "ava@mergington.edu"]
        },
        "Math Olympiad": {
            "description": "Advanced math problems, competitions, and team practice",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 14,
            "participants": ["sophia@mergington.edu", "williams@mergington.edu"]
        }
    }

    activities.clear()
    activities.update(initial_activities)

    yield

    activities.clear()
    activities.update(initial_activities)
