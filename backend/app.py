from flask import Flask, jsonify
from services import fetch_asteroid_data
from analysis import categorize_hazard_level, filter_asteroids

app = Flask(__name__)

# fetch data:
df = fetch_asteroid_data()

# perform analysis:
average_speed = df['speed( km/h )'].astype(float).mean()
df = categorize_hazard_level(df)

# Print or log the average speed if you want to see it
print(f"The average speed of all asteroids is {average_speed} km/h")

@app.route('/dangerous_asteroids')
def dangerous_asteroids():
    filtered_asteroids = filter_asteroids(df)
    return jsonify(filtered_asteroids.to_dict(orient='records'))

if __name__ == "__main__":
    app.run()
