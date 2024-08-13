import paho.mqtt.client as mqtt
import json
import random
import time

# MQTT Broker settings
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "status/update"

def generate_status():
    return {"status": random.randint(0, 6)}

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with code {rc}")

def publish_status():
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    try:
        while True:
            status = generate_status()
            client.publish(MQTT_TOPIC, json.dumps(status))
            print(f"Published: {status}")
            time.sleep(1)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    publish_status()
