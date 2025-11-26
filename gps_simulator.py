import random
import time
import json
from mqtt_client import send_message

def simulate_gps():
    lat, lon = 28.7041, 77.1025

    while True:
        lat += random.uniform(-0.0005, 0.0005)
        lon += random.uniform(-0.0005, 0.0005)
        payload = {"lat": lat, "lon": lon, "timestamp": time.time()}
        send_message(json.dumps(payload))
        time.sleep(0.1)

simulate_gps()