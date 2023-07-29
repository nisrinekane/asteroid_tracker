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
        data = response.json()
        print(data['near_earth_objects'][0])  # Print out the first asteroid's data

        response.raise_for_status()
    except RequestException as e:
        print(f'failed to fetch asteroid data: {e}')
        return None
    
    try:
        data = response.json()
    except ValueError as e:
        print('Failed to parse asteroid data')
        return None
    
    # near earth objects firld:
    asteroids = data.get('near_earth_objects', [])

    # commvert data to pd df:
    df = pd.DataFrame(asteroids)

    return df
    # return data

if __name__ == "__main__":
    fetch_asteroid_data()
