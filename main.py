import requests
import os
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": -15.601411,
    "lon": -56.097893,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()

print(response.status_code)
weather_data = response.json()
print(weather_data["list"])

#get id for each check
will_rain = False
for x in weather_data["list"]:
    weather_id = x["weather"][0]["id"]
    print(weather_id)
    if weather_id < 600:
        will_rain =True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella ☔",
        from_="+18889953087",
        to="+18777804236",
    )
    print(message.status)
    print("It will rain")

#works via virtual phone, not through actual numbers based on verification restrictions
