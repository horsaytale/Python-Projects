#https://www.nutritionix.com/business/api
#https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#
#https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.gz6pu9o7f9iz
#https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.zhjgcprrgvim
#https://dashboard.sheety.co/projects/61d3d2c527dad22cae0ce1f6
#https://sheety.co/docs/requests
#https://sheety.co/docs/authentication.html
#https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
#https://docs.python-requests.org/en/master/user/authentication/#basic-authentication

import requests
from datetime import datetime
import os

API_KEY="6a128dbb3f2e1b385022ee94b5a31118"
APP_ID="e283db25"

basic_header={
    "Authorization": "Basic YW1iZXIxOTk1OkwhbVNoIWVIdSExOTk1"
}
bearer_header={
    "Authorization": "Bearer aieq$Qsad(R10239vasdsdd23"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f42d88fb12ca54af64e0e48dd6ab35e3/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_header)

    print(sheet_response.text)
