import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
SHEET_ENDPOINT = os.environ['sheety_endpoint']
PASSWORD = os.environ['PASSWORD']
USERNAME = os.environ['USERNAME']
API_KEY = os.environ['API_KEY']
APP_ID = os.environ['APP_ID']

GENDER = "M"
WEIGHT = 64
HEIGHT = 195
AGE = 22

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# Getting input to process from the user
exercise_text = input("What exercise did you do today?")

# Setting headers for the request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Setting parameters for the request
exercise_params = {
    "query": exercise_text,
    "gender": "M",
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

# Doing a POST Request to the exercise endpoint and getting the data about the input
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

# Step-4-Saving data into Google Sheets

# Storing the nutrition API values in a list
result_list = result["exercises"]
print(result_list)

# Getting today's date and time
today = datetime.now()
today_formatted = today.strftime("%d/%m/%Y")
now = today.strftime("%X")

# For all items in result list getting the required parameters and making a POST request to sheety

# Step-5 : Authentication

basic = HTTPBasicAuth(USERNAME, PASSWORD)

for exercise in result_list:
    sheet_params = {
        "workout": {
            "date": today_formatted,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_params, auth=basic)
    print(sheet_response.text)