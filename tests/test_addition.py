from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_addition_endpoint():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[1,2],[3,4]]})
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data


def test_empty_payload():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": []})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == []
    assert data["status"] == "complete"


def test_invalid_payload():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": "invalid"})
    assert response.status_code == 422


def test_single_empty_list():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[]]})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [0]
    assert data["status"] == "complete"


def test_nested_empty_list():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[], [1, 2], [], [3, 4]]})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [0, 3, 0, 7]
    assert data["status"] == "complete"


def test_invalid_nested_lists():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[1, 2], "invalid", [3, 4]]})
    assert response.status_code == 422


def test_large_numbers():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[10**9, 10**9], [10**9, 10**9]]})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [2*(10**9), 2*(10**9)]
    assert data["status"] == "complete"


def test_negative_numbers():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[1, -2], [-3, 4]]})
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [-1, 1]
    assert data["status"] == "complete"


def test_missing_batchid():
    response = client.post("/api/add", json={"payload": [[1, 2], [3, 4]]})
    assert response.status_code == 422


def test_missing_payload():
    response = client.post("/api/add", json={"batchid": "id0101"})
    assert response.status_code == 422


def test_incorrect_batchid_type():
    response = client.post("/api/add", json={"batchid": 101, "payload": [[1, 2], [3, 4]]})
    assert response.status_code == 422


def test_incorrect_payload_type():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": "not a list"})
    assert response.status_code == 422


def test_incorrect_nested_payload_type():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[1, "two"], [3, 4]]})
    assert response.status_code == 422


def test_response_structure():
    response = client.post("/api/add", json={"batchid": "id0101", "payload": [[1,2],[3,4]]})
    assert response.status_code == 200
    data = response.json()
    assert "batchid" in data
    assert "response" in data
    assert "status" in data
    assert "started_at" in data
    assert "completed_at" in data
