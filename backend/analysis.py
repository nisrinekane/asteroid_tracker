import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# func to calculate avg speed of asteroids:
def calculate_average_speed(df):
    df['average_speed'] = df['speed( km/h )']
    return df

# func to categorize asteroids based on hazard level:
def categorize_hazard_level(df):
    bins = [-np.inf, 0, 10, 20, np.inf]
    labels = ['no hazard', 'low hazard', 'medium hazard', 'high hazard']
    df['hazard_category'] = pd.cut(df['average_speed'], bins=bins, labels=labels)
    return df

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
    return close_asteroids

# load data:
def load_data(filename):
    data = pd.read_json(filename)
    # format data:
    data['speed( km/h )'] = data['close_approach_data'].apply(lambda x: x[0]['relative_velocity']['kilometers_per_hour'])
    data['close_approach_date'] = data['close_approach_data'].apply(lambda x: x[0]['close_approach_date'])
    data['is_potentially_hazardous_asteroid'] = data['is_potentially_hazardous_asteroid']
    return data

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
