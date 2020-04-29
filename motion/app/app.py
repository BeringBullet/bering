# https://tutorials-raspberrypi.com/raspberry-pi-door-window-sensor-with-reed-relais/
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import threading
from homie.device_boolean import Device_Boolean


mqtt_settings = {
    "MQTT_BROKER": "192.168.86.39",
    "MQTT_PORT": 1883,
}

deviceID = "gd1-motion"
MQTT_PUBLISH_DELAY = 2
GPIO_pin = 14

GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers
GPIO.setup(GPIO_pin, GPIO.IN)  # GPIO Assign mode

switch = Device_Boolean(device_id=deviceID, name="Motion 1", mqtt_settings=mqtt_settings)

def send_State(value):
    if lastvalue != value:
        lastvalue = value
        print("mqtt: " + str(value))
        if value == 0:
            switch.update_boolean(False)
        else:
            switch.update_boolean(True)
        lastvalue = value


def main():
    publish_homeassistant(switch)
    motionTrue = False
    while True:
        if GPIO.input(GPIO_pin) == True:  # If GPIO_pin pin goes high, motion is detected
            if (motionTrue == False):
                print("Motion Detected!")
                switch.update_boolean(True)
            motionTrue = True
        else:
            if (motionTrue):
                #print("waiting 7 sec to check before closing")
                time.sleep(7)
                if GPIO.input(GPIO_pin) != True:
                    if (motionTrue):
                        print("NO Motion Detected!")
                        switch.update_boolean(False)
                    motionTrue = False
        time.sleep(MQTT_PUBLISH_DELAY)


def publish_homeassistant(device):
    hass_config = f'homeassistant/sensor/{deviceID}/config'
    hass_payload = f'{{"name": {device.name}","state_topic": "homie/{device.device_id}/boolean/boolean"}}'

    client = mqtt.Client(deviceID)  # create new instance
    client.connect("192.168.86.39")  # connect to broker
    client.publish(hass_config, hass_payload)  # publish


if __name__ == '__main__':
    main()
