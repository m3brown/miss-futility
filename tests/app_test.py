from app import app


def test_app_returns_200():
    # Arrange
    client = app.test_client()
    # client.testing = True

    # Act
    result = client.get("/")

    # Assert
    assert result.status_code == 200


def test_app_page_has_expected_text():
    # Arrange
    client = app.test_client()

    # Act
    result = client.get("/")

    # Assert
    assert "Before you commit, every commit!" in str(result.data)
