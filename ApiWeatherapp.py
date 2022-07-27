import requests
from pytz import timezone
from datetime import datetime

API_KEY = "Your API KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a City Name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
print()
print(response)
print()

if response.status_code == 200:
    data = response.json()
    print(data)
    print()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15 ,2)
    windspeed = data["wind"]["speed"]
    sunrise = data["sys"]["sunrise"]
    humidity = data["main"]["humidity"]

    # timestamp
    ts = sunrise

    sunset = data["sys"]["sunset"]
    # timestamp1
    ts1 = sunset

    print("Weather:", weather)
    print("Temperature:", temperature, "Celsius")
    print("Humidity: ", humidity, "%")
    print("Wind speed: ", windspeed, "kn")

    # converting unix weather sunrise and sunset format to another more readable format.
    print("Sunrise: " + datetime.fromtimestamp(ts, timezone("YourTimeZone")).strftime("%Y-%m-%d %H:%M:%S"))
    print("Sunset: " + datetime.fromtimestamp(ts1, timezone("YourTimeZone")).strftime("%Y-%m-%d %H:%M:%S"))
else:
    print("An error occurred.")