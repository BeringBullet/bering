import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
from datetime import datetime

BROCKER_ADDRESS = "192.168.86.30"
MQTT_TOPIC_HUMIDITY = "home/GS1/humidity"
MQTT_TOPIC_TEMPERATURE = "home/GS1/temperature"
MQTT_TOPIC_STATE = "home/GS1/status"
MQTT_PUBLISH_DELAY = 60
MQTT_CLIENT_ID = "dht22"

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

print("creating new instance")
client = mqtt.Client(MQTT_CLIENT_ID)  # create new instance
print("connecting to broker")
client.connect(BROCKER_ADDRESS)  # connect to broker


def sendMessage(topic, payload):
    client.publish(topic, payload)


def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    sendMessage(MQTT_TOPIC_TEMPERATURE, temperature)
    sendMessage(MQTT_TOPIC_HUMIDITY, humidity)
    print(temperature)


def main_thread():
    time.sleep(MQTT_PUBLISH_DELAY)
    get_sensor_data()


def main():
    while True:
        main_thread()


if __name__ == '__main__':
    main()
