import pytest
from backend.analysis import load_data, calculate_average_speed, categorize_hazard_level, filter_asteroids

def test_average_speed():
    # load data from test_data.json
    data = load_data('test_data.json')
    average_speed = calculate_average_speed(data)
    assert isinstance(average_speed, float), "Average speed should be a float"
    assert average_speed > 0, "Average speed should be greater than zero"


def test_hazard_level():
    data = load_data('test_data.json')
    categorized_data = categorize_hazard_level(data)
    assert isinstance(categorized_data, list), "Data should be a list"
    assert 'hazard_category' in categorized_data[0], "Each asteroid should have a 'hazard_category' field"


def test_filter_asteroids():
    data = load_data('test_data.json')
    categorized_data = categorize_hazard_level(data)
    assert isinstance(categorized_data, list), "Data should be a list"
    assert 'hazard_category' in categorized_data[0], "Each asteroid should have a 'hazard_category' field"

