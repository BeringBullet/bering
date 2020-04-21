#!/usr/bin/python3

from flask import Flask
#import json

app = Flask(__name__)


#class Device:
#    BROCKER_ADDRESS = "192.168.86.30"
#    MQTT_TOPIC_HUMIDIT = "home/GS1/humidity"
#    MQTT_TOPIC_TEMPERATURE = "home/GS1/temperature"
#    MQTT_TOPIC_STATE = "home/GS1/status"
#    MQTT_PUBLISH_DELAY = 10
#    MQTT_CLIENT_ID = "dht22"
#    DHT_PIN = 4
#

@app.route('/')
def hello_world():
    return 'Hello, World!'


#@app.route('/sensors/<sensors_ID>', methods=['POST'])
#def json():
#    device = Device()
#    return json.dump(device)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
