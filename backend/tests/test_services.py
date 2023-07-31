from backend.services import fetch_asteroid_data

def test_fetch_asteroid_data():
    data = fetch_asteroid_data()
    assert data is not None, "Data should not be None"
    assert "name" in data.columns, "Data should have a 'name' column"
    assert "speed( km/h )" in data.columns, "Data should have a 'speed( km/h )' column"
    assert "is_potentially_hazardous_asteroid" in data.columns, "Data should have an 'is_potentially_hazardous_asteroid' column"


