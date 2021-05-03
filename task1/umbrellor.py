from datetime import datetime

import requests


def main(args):
    city = args.get("city", "Berlin")
    weather = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
    description = weather.json()["description"]
    umbrella = "No"
    if "rain" in description.lower():
        umbrella = "Yes"
    print(f"{str(datetime.now())}: Should I bring an umbrella? {umbrella}.")
    print(weather.json())
    return {
        "Should I bring an umbrella?": umbrella,
        "timestamp": str(datetime.now()),
    }
