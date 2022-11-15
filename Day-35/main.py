import requests
import smtplib
api_key = "69f04e4613056b159c2761a9d9e664d2"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_EMAIL = "adithya.mailbot@gmail.com"
PASSWORD = "bashpyjrfaocrkdu"

weather_parameters = {
    "lat": 13.117230,
    "lon": 80.215149,
    "appid": api_key,

}

# Getting API request with the above-mentioned parameters
response = requests.get(OWM_Endpoint, params=weather_parameters)
# Raising exceptions if any
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
# Getting the current 12 hour data by Slicing
weather_slice = weather_data["hourly"][:12]
print(weather_slice)
will_rain = False
# Going through the data and slicing the 12 hour data and checking whether it will rain
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True



if will_rain:
    print("Bring an Umbrella.")
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)  # Logging in using username and password
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="adist1340@gmail.com",
            msg=f"Subject:Take an Umbrella\n\nIt's going to rain! Take an Umbrella☔"
        )  # sending mail with from
    # address, to address and message
# Getting the weather id of current
# print(weather_data["hourly"][0]["weather"][0]["id"])


