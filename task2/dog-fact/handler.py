import requests


def handle(req):
    """
    Returns a fun dog fact
    :param req: None
    :return: A dog fact
    """
    dog_fact_request = requests.get(
        "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
    )
    dog_fact = dog_fact_request.json()[0]["fact"]
    dog_sentence = f"Here's a fun dog fact: {dog_fact}"
    print(dog_sentence)
    return dog_sentence
