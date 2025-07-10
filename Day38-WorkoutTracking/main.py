import requests
from datetime import datetime
import os

NUTRITIONIX_API_ID = '44f4f260'
NUTRITIONIX_API_KEY = '8bfcb371c4f0c15cedf4481272fa72cb'
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_TOKEN = 'tester98'
SHEETY_ENDPOINT = 'https://api.sheety.co/ae89495f4e462eca1451796701974fdb/workoutTracking/workouts'

user_input = input('Tell me which exercises you did: ')

headers = {
    'x-app-id': NUTRITIONIX_API_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
}

params = {
    'query': user_input,
    'weight_kg': 68,
    'height_cm': 182,
    'age': 35,
}

nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=params)
nutritionix_data = nutritionix_response.json()

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in nutritionix_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_headers = {'Authorization': f'Bearer {SHEETY_TOKEN}'}

sheety_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
