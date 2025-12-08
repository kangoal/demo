"""
Tests for the server module.
"""

import pytest
from fastapi.testclient import TestClient
from src import app


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


class TestServer:
    """Test cases for the FastAPI server."""

    def test_root_endpoint(self, client):
        """Test the root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data

    def test_health_endpoint(self, client):
        """Test the health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "version" in data
        assert "timestamp" in data

    def test_calculate_add(self, client):
        """Test the calculate endpoint with addition."""
        response = client.post("/calculate", json={
            "operation": "add",
            "a": 5,
            "b": 3
        })
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "add"
        assert data["result"] == 8
        assert data["success"] is True

    def test_calculate_divide_by_zero(self, client):
        """Test division by zero returns error."""
        response = client.post("/calculate", json={
            "operation": "divide",
            "a": 5,
            "b": 0
        })
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is False
        assert "Cannot divide by zero" in data["error"]

    def test_calculate_invalid_operation(self, client):
        """Test invalid operation returns 400."""
        response = client.post("/calculate", json={
            "operation": "invalid",
            "a": 5,
            "b": 3
        })
        assert response.status_code == 400

    def test_operations_endpoint(self, client):
        """Test the operations list endpoint."""
        response = client.get("/operations")
        assert response.status_code == 200
        data = response.json()
        assert "operations" in data
        assert len(data["operations"]) > 0
        assert data["operations"][0]["name"] == "add"
