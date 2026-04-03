"""FastAPI endpoint tests for the Mergington High School API."""

import pytest


class TestRootEndpoint:
    def test_root_redirects(self, client):
        # Arrange
        expected_location = "/static/index.html"

        # Act
        response = client.get("/", follow_redirects=False)

        # Assert
        assert response.status_code == 307
        assert response.headers["location"] == expected_location


class TestGetActivities:
    def test_get_activities(self, client, reset_activities):
        # Arrange

        # Act
        response = client.get("/activities")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "Chess Club" in data
        assert "Programming Class" in data

    def test_activity_data_format(self, client, reset_activities):
        # Act
        response = client.get("/activities")
        activities = response.json()

        # Assert
        required_keys = {"description", "schedule", "max_participants", "participants"}
        for activity in activities.values():
            assert required_keys.issubset(activity.keys())
            assert isinstance(activity["participants"], list)
            assert isinstance(activity["max_participants"], int)


class TestSignupEndpoint:
    def test_successful_signup(self, client, reset_activities):
        # Arrange
        activity_name = "Chess Club"
        email = "newstudent@mergington.edu"

        # Act
        response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

        # Assert
        assert response.status_code == 200
        message = response.json()["message"]
        assert email in message
        assert activity_name in message

    def test_signup_duplicate(self, client, reset_activities):
        # Arrange
        activity_name = "Chess Club"
        existing_email = "michael@mergington.edu"

        # Act
        response = client.post(f"/activities/{activity_name}/signup", params={"email": existing_email})

        # Assert
        assert response.status_code == 400
        assert "already signed up" in response.json()["detail"].lower()

    def test_signup_nonexistent_activity(self, client, reset_activities):
        # Arrange
        activity_name = "NotReal Club"

        # Act
        response = client.post(f"/activities/{activity_name}/signup", params={"email": "x@x.com"})

        # Assert
        assert response.status_code == 404
        assert "activity not found" in response.json()["detail"].lower()


class TestUnregisterEndpoint:
    def test_successful_unregister(self, client, reset_activities):
        # Arrange
        activity_name = "Chess Club"
        email = "michael@mergington.edu"

        # Act
        response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

        # Assert
        assert response.status_code == 200
        assert "unregistered" in response.json()["message"].lower()

    def test_unregister_nonexistent_student(self, client, reset_activities):
        # Arrange
        activity_name = "Chess Club"

        # Act
        response = client.post(f"/activities/{activity_name}/unregister", params={"email": "nobody@mergington.edu"})

        # Assert
        assert response.status_code == 400
        assert "not registered" in response.json()["detail"].lower()

    def test_unregister_nonexistent_activity(self, client, reset_activities):
        # Act
        response = client.post("/activities/NotReal/unregister", params={"email": "a@b.com"})

        # Assert
        assert response.status_code == 404
        assert "activity not found" in response.json()["detail"].lower()
