from datetime import datetime

import requests


def main(args):
    """
    Method for checking whether one should bring an umbrella in a specific city.
    :param args: dictionary with a city as a value for key "city". (Berlin used as a default)
    :return: Dictionary containing timestamp and whether one should bring an umbrella. (yes/no)
    """
    city = args.get("city", "Berlin")
    # fetch api
    weather = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
    # get weather description
    description = weather.json()["description"]
    umbrella = "No"
    # if description contains rain, say "yes"
    if "rain" in description.lower():
        umbrella = "Yes"
    print(f"{str(datetime.now())}: Should I bring an umbrella? {umbrella}.")
    print(weather.json())
    return {
        "Should I bring an umbrella?": umbrella,
        "timestamp": str(datetime.now()),
    }
