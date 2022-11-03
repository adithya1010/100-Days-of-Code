import requests
from datetime import datetime
MY_LAT = "13.117230"
MY_LONG = "80.215149"
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")  # Getting API request and storing it in a
# # variable
#
# response.raise_for_status()  # Raising exceptions if one occurs
#
#
# # Getting longitude and latitude and storing it in variables
# latitude = response.json()["iss_position"]["latitude"]  # Getting the JSON data and storing it in a variable
# longitude = response.json()["iss_position"]["longitude"]
#
# # Converting longitude and latitude to tuple format
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise)
print(sunset)

print(time_now.hour)

# If the ISS is close to my current location
# and it is currently dark
# then send me an email to look up

