from fastapi.testclient import TestClient
from api import app


client = TestClient(app)

def test_create_and_list_flights():
    response = client.post("/flights", json={
        "FlightNo": "0085",
        "Origin": "DEL",
        "Destination": "MAX",
        "DATE": "2025-10-29"
    })
    assert response.status_code == 200
    assert response.json()["FlightNo"] == "0085"

    response = client.get("/flights")
    assert response.status_code == 200
    flights = response.json()

    assert any(f["FlightNo"] == "0085" for f in flights)