import requests
from requests.exceptions import RequestException
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
NASA_API_KEY = os.getenv('NASA_API_KEY')

def fetch_asteroid_data():
    try:
        response = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={NASA_API_KEY}', timeout=10)

        response.raise_for_status()
    except RequestException as e:
        print(f'failed to fetch asteroid data: {e}')
        return None
    
    try:
        data = response.json()
    except ValueError as e:
        print('Failed to parse asteroid data')
        return None
    
    # near earth objects field:
    asteroids = data.get('near_earth_objects', [])

    # Convert each asteroid into the format expected by analysis.py
    formatted_asteroids = []
    for asteroid in asteroids:
        close_approach_data = asteroid.get('close_approach_data', [{}])[0]
        formatted_asteroids.append({
            'name': asteroid.get('name'),
            'speed( km/h )': close_approach_data.get('relative_velocity', {}).get('kilometers_per_hour', '0'),
            'close_approach_date': close_approach_data.get('close_approach_date'),
            'is_potentially_hazardous_asteroid': asteroid.get('is_potentially_hazardous_asteroid', False),
        })

    # Convert data to pd df:
    df = pd.DataFrame(formatted_asteroids)

    return df


if __name__ == "__main__":
    fetch_asteroid_data()
