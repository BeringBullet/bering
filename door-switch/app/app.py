#https://tutorials-raspberrypi.com/raspberry-pi-door-window-sensor-with-reed-relais/
import RPi.GPIO as GPIO
import time
from homie.device_boolean import Device_Boolean


mqtt_settings = {
    "MQTT_BROKER": "192.168.86.30",
    "MQTT_PORT": 1883,
}

deviceID = "gd1"
MQTT_PUBLISH_DELAY = 60
MAGNET_GPIO = 17
lastvalue = -1

def my_callback(value):
    value = GPIO.input(value)
    print("new: " + str(value) + " old: " + str(lastvalue))
    if lastvalue != value:
        send_State(value)
        

GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers
GPIO.setup(MAGNET_GPIO, GPIO.IN)  # GPIO Assign mode
GPIO.add_event_detect(MAGNET_GPIO, GPIO.BOTH, callback=my_callback)

switch = Device_Boolean(
    device_id=deviceID, name="Switch 1", mqtt_settings=mqtt_settings)

def send_State(value):
    print("mqtt: " + str(value))
    if value == 0:
        switch.update_boolean(True)
    else:
        switch.update_boolean(False)
    lastvalue = value
    print("new: " + str(value) + " old: " + str(lastvalue))
   

def main_thread():
    send_State(GPIO.input(MAGNET_GPIO))
    time.sleep(MQTT_PUBLISH_DELAY)

def main():
    publish_homeassistant(switch)
    while True:
        main_thread()

def publish_homeassistant(device):
    hass_config = f'homeassistant/sensor/{deviceID}/config'
    hass_payload = f'{{"name": {device.name}","state_topic": "homie/{device.device_id}/boolean/boolean"}}'

    client = mqtt.Client(deviceID)  # create new instance
    client.connect("192.168.86.30")  # connect to broker
    client.publish(hass_config, hass_payload)  # publish

if __name__ == '__main__':
    main()
