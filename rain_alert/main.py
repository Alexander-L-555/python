import requests
import os
from twilio.rest import Client

api_key = "07fcecfade77cb53876862a43790da31"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC3ca4c3230f96d107384c606854340dd3"
auth_token = "af41c7dd22ecc5f4423cb7e80dcd6559"

weather_params = {
    "lat": 28.318541,
    "lon": -81.542389,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
       will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="Get an umbrella, it's gonna rain.",
        from_='+14696544965',
        to='+19045818857'
    )
    print(message.status)
