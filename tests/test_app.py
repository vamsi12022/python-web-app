import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Check if the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"AI Agent" in response.data

def test_health_endpoint(client):
    """Check if the health API returns JSON UP."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == "UP"