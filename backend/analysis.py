import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

# func to calculate avg speed of asteroids:
def calculate_average_speed(data):
    total_speed = 0
    num_asteroids = len(data)
    for asteroid in data:
        asteroid_speed = asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
        total_speed += float(asteroid_speed)  # ensure speed is treated as a number
    average_speed = total_speed / num_asteroids if num_asteroids > 0 else 0
    return average_speed



# func to categorize asteroids based on hazard level:
def categorize_hazard_level(data):
    bins = [-np.inf, 0, 10, 20, np.inf]
    labels = ['no hazard', 'low hazard', 'medium hazard', 'high hazard']
    
    for asteroid in data:
        asteroid_speed = float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
        asteroid['hazard_category'] = pd.cut([asteroid_speed], bins=bins, labels=labels)[0]
        
    return data


# filter asteroids:
def filter_asteroids(data):
    # hazardous asteroids:
    dangerous_asteroids = data[data['is_potentially_hazardous_asteroid']]
    # filter by close approach date:
    one_month_from_now = datetime.now() + timedelta(days=30)
    close_asteroids = dangerous_asteroids[
        dangerous_asteroids['close_approach_date'].apply(
            lambda x: datetime.fromisoformat(x) < one_month_from_now
        )]
    print(close_asteroids)
    return close_asteroids

# load data func:
def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def process_data(data):
    result = []
    for asteroid in data:
        name = asteroid["name"]
        speed = float(asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"])
        is_hazardous = asteroid["is_potentially_hazardous_asteroid"]
        result.append((name, speed, is_hazardous))
    return result


# main function:
def main():
    # load data:
    data = load_data('asteroids.json')
    # calculate average speed:
    data = calculate_average_speed(data)
    # categorize hazard level:
    data = categorize_hazard_level(data)
    # filter asteroids:
    filtered_asteroids = filter_asteroids(data)
    print(filtered_asteroids)

if __name__ == "__main__":
    main()
