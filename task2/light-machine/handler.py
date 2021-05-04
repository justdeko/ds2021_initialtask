import os
import time
import magichue


def handle(req):
    """
    Lets the lights in my room (or any room with a magichue for that matter) flash according to the request body
    :param req: the request string:
    :return:
    """
    # red blue and green rgb values
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    # get the light
    ip = os.getenv("light_ip", "127.0.0.1")
    light = magichue.Light(ip)

    # turn turn lights on if they aren't set them to "white" (default color)
    if not light.on:
        light.on = True
        light.rgb = (255, 255, 255)
        time.sleep(1)

    # flash the lights for a second in the specific request color (good, bad or neutral), then go back to white
    if "bad" in req:
        light.rgb = red
    elif "good" in req:
        light.rgb = green
    else:
        light.rgb = blue
    time.sleep(1)
    light.rgb = (255, 255, 255)

    return "Lights flashed"
