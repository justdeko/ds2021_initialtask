import json
import os
import sys

import requests


def handle(req):
    """
    Based on the sentiment of the email, send a response in a positive/negative/neutral manner.
    :param req: the email body and sentiment
    :return: whether the email was sent successfully
    """

    # handle request
    payload = json.loads(req)
    if not payload["body"] or not payload["sentiment"]:
        sys.exit("Response is wrong")
    sentiment = payload["sentiment"]
    body = payload["body"]

    # get the webhook url
    url = os.getenv("email_webhook", "127.0.0.1")

    # Generate response
    response_body = "I'll get back to you soon."
    if "bad" in sentiment:
        response_body = "Woah, don't be that rude!"
    elif "good" in sentiment:
        response_body = "Thank you a lot for this email, very nice from you! I'll get back to you as soon as I can."

    reply = requests.post(
        url, data={"response_body": response_body, "search_body": body}
    )
    if reply.status_code == 200:
        return "Email sent."
    else:
        return "Sending email failed."
