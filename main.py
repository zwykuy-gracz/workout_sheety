import requests
from datetime import datetime as dt

APP_ID = 'a'
API_KEY = 'b'

today = dt.now()

user_input = input("What exercise? ")

query = {
    'query': user_input
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
# exercise_endpoint = 'http://v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/c/workoutTracking/workouts'

response = requests.post(url=exercise_endpoint, json=query, headers=headers)
results = response.json()
print(results)

sheety_headers = {
    'Authorization': 'Bearer d',
}

workout = {
    'workout': {
        'date': today.strftime("%d/%m/%Y"),
        'time': today.strftime("%X"),
        'exercise': str(results["exercises"][0]["name"]).title(),
        'duration': round(results["exercises"][0]["duration_min"]),
        'calories': round(results["exercises"][0]["nf_calories"]),
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=workout, headers=sheety_headers)
print(sheety_response.text)