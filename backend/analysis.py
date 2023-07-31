import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

# func to calculate avg speed of asteroids:
# def calculate_speed(data):
#     def get_speed(asteroid):
#         close_approach_data = asteroid['close_approach_data']
#         if isinstance(close_approach_data, list) and len(close_approach_data) > 0:
#             speed = close_approach_data[0]['relative_velocity']['kilometers_per_hour']
#             return float(speed)
#         else:
#             return np.nan

#     data['average_speed'] = data.apply(get_speed, axis=1)
#     return data
def calculate_speed(data):
    # Convert speed values to float
    data['speed( km/h )'] = data['speed( km/h )'].astype(float)
    # Calculate average speed and add it as a new column
    data['average_speed'] = data['speed( km/h )'].mean()
    return data




# func to categorize asteroids based on hazard level:
def categorize_hazard_level(data):
    bins = [-np.inf, 0, 10, 20, np.inf]
    labels = ['no hazard', 'low hazard', 'medium hazard', 'high hazard']
    
    def categorize(asteroid):
        asteroid_speed = float(asteroid['speed( km/h )'])
        return pd.cut([asteroid_speed], bins=bins, labels=labels)[0]

    data['hazard_category'] = data.apply(categorize, axis=1)
        
    return data



# filter asteroids:
# filter asteroids:
def filter_asteroids(data):
    # hazardous asteroids:
    dangerous_asteroids = data[data['is_potentially_hazardous_asteroid']]
    # filter by close approach date:
    one_month_from_now = pd.to_datetime('now') + pd.DateOffset(months=1)
    close_asteroids = dangerous_asteroids[
        dangerous_asteroids['close_approach_date'].apply(
            lambda x: pd.to_datetime(x) < one_month_from_now
        )]
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
