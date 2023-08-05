import requests

MY_API_KEY = "4f30148bdfdc0dbb52da3376395983a0"
OWN_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,

    "appid": MY_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_ENDPOINT,params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella") 