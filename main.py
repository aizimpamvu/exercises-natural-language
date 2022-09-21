import requests

APP_ID = "5d7e788b"
API_KEY = "4d7546e84e2809c416d08abdd4e07a97"

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercises_data = {
    "query": input("Tell which exercises you did? "),
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=nutrition_endpoint, json=exercises_data, headers=headers)
print(response.text)
