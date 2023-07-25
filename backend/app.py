from flask import Flask
from services import fetch_asteroid_data
from analysis import calculate_average_speed, categorize_hazard_level

app = Flask(__name__)

# fetch data:
df = fetch_asteroid_data()

# perform analysis:
df = calculate_average_speed(df)
df = categorize_hazard_level(df)

# @app.route('/')
# def home():
#     return 'Home'