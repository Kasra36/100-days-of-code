import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
NUTRITIONIX_API_ID = os.getenv('NUTRITIONIX_API_ID')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_ID = os.getenv('SHEETY_ID')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
SHEETY_ENDPOINT = f'https://api.sheety.co/{SHEETY_ID}/workoutTracking/workouts'

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
