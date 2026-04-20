def test_get_activities_returns_seed_data(client):
    # Arrange

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert response.status_code == 200
    assert "Chess Club" in activities
    assert "Programming Class" in activities
    assert activities["Chess Club"]["max_participants"] == 12
    assert activities["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]