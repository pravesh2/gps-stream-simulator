import paho.mqtt.client as mqtt

client = mqtt.Client("gps_simulator")
client.connect("broker.hivemq.com", 1883)

def send_message(msg):
    client.publish("devnullx/gps", msg)