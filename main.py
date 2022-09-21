import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 64
HEIGHT_CM = 172
AGE = 25
APP_ID = "5d7e788b"
API_KEY = "4d7546e84e2809c416d08abdd4e07a97"

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/7750c695b8c1e162e1f101796a478713/workoutTracking/workouts"

text_answer= input("Tell which exercises you did? ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercises_data = {
    "query": text_answer,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=nutrition_endpoint, json=exercises_data, headers=headers)
# new_response = requests.post(url=sheety_endpoint, json=sheety_config, headers=headers)
result = response.json()
# print(result["exercises"])


today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_input ={
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_input)

    print(sheet_response.text)