import pandas as pd
import numpy as np

# func to calculate avg speed of asteroids:
def calculate_average_speed(df):
    df['average_speed'] = (df['speed( km/h )'] / df['close_approach_date']).astype(float)
    return df

# func to categorize asteroids based on hazard level:
def categorize_hazard_level(df):
    bins = [-np.inf, 0, 10, 20, np.inf]
    labels = ['no hazard', 'low hazard', 'medium hazard', 'high hazard']
    df['hazard_category'] = pd.cut(df['average_speed'], bins=bins, labels=labels)
    return df