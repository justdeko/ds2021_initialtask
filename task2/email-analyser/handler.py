import json
import os
import sys

import requests


def handle(req):
    """
    Analyses the sentiment of an email, acts accordingly.
    :param req:  a json containing at least "body" as a key-value pair.
    :return:
    """

    # get the email payload, return if it's not there
    payload = json.loads(req)
    if not payload["body"]:
        sys.exit("Response is wrong")

    gateway_hostname = os.getenv("gateway_hostname", "gateway")

    # perform sentiment analysis
    res = requests.post(
        "http://" + gateway_hostname + ":8080/function/sentimentanalysis",
        data=payload["body"],
    )
    if res.status_code != 200:
        sys.exit(
            "Sentiment analysis failed, expected: %d, got: %d\n"
            % (200, res.status_code)
        )

    polarity = res.json()["polarity"]

    # simplify the sentiment to bad/neutral/good
    sentiment = "neutral"
    if polarity < -0.5:
        sentiment = "bad"
    elif polarity > 0.5:
        sentiment = "good"

    # send signal to my lights
    requests.post(
        "http://" + gateway_hostname + ":8080/function/light-machine",
        data=sentiment,
    )

    # if i need cheering up, send me a dog fact
    if sentiment == "bad":
        requests.post(
            "http://" + gateway_hostname + ":8080/function/dog-fact",
            data=sentiment,
        )

    return sentiment
