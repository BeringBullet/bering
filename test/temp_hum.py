import paho.mqtt.client as mqtt
import time
from datetime import datetime

broker_address = "192.168.86.30"
clientName = "mainbase"

MQTT_TOPIC_HUMIDITY = "garage/1/humidity"
MQTT_TOPIC_TEMPERATURE = "garage/1/temperature"
MQTT_TOPIC_STATE = "garage/1/status"
MQTT_PUBLISH_DELAY = 10
MQTT_CLIENT_ID = "dht22"

print("creating new instance")
client = mqtt.Client(clientName)  # create new instance

def connect():
    print("connecting to broker")
    client.connect(broker_address)  # connect to broker

def sendMessage(msg):
    client.publish(str(msg), payload=53)


def testmsg():
    now = datetime.now()
    msg = MQTT_TOPIC_HUMIDITY
    return msg


def main_thread():
    time.sleep(MQTT_PUBLISH_DELAY)
    sendMessage(testmsg())

def main():
    connect()
    while True:
        main_thread()

if __name__ == '__main__':
    main()
