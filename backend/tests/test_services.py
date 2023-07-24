from backend.services import fetch_asteroid_data

def test_fetch_asteroid_data():
    data = fetch_asteroid_data()
    assert data is not None, "Data should not be None"
    assert "near_earth_objects" in data, "Data should have a 'near_earth_objects' field"


