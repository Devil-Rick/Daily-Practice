import config
import requests as req
from datetime import datetime as dt

# -------------------- Getting today's Date --------------------- #
today = dt.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

# -------------------- Getting the calorie data --------------------- #
calorie_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
calorie_header = {
    "x-app-id": config.NUTRI_APP_ID,
    "x-app-key": config.NUTRI_API_KEY,
}
calorie_body = {
    "query": input("Enter today's exercise: "),
    # "gender": "female",
    # "weight_kg": 72.5,
    # "height_cm": 167.64,
    # "age": 30
}
calorie_response = req.post(calorie_endpoint, headers=calorie_header, json=calorie_body)
calorie_output = calorie_response.json()
print()

# -------------------- Updating the data in Sheets --------------------- #
sheet_endpoint = "https://api.sheety.co/de57b105b38f0d3ffc8bebf1c6976c7e/day39Project(workout)/workouts"
sheet_body = {
    'workout': {
      'date': today_date,
      'time': today_time,
      'exercise': calorie_output["exercises"][0]["name"].capitalize(),
      'duration': calorie_output["exercises"][0]["duration_min"],
      'calories': calorie_output["exercises"][0]["nf_calories"]
    }
}
sheet_response = req.post(sheet_endpoint, json=sheet_body)
