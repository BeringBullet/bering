#https://tutorials-raspberrypi.com/raspberry-pi-door-window-sensor-with-reed-relais/
import Adafruit_DHT
import time
from homie.device_boolean import Device_Boolean

mqtt_settings = {
    "MQTT_BROKER": "192.168.86.30",
    "MQTT_PORT": 1883,
}

deviceID = "gd1"
MQTT_PUBLISH_DELAY = 60
MAGNET_GPIO = 17

GPIO.setup(MAGNET_GPIO, GPIO.IN)  # GPIO Assign mode

switch = Device_Boolean(
    device_id=deviceID, name="Switch 1", mqtt_settings=mqtt_settings)


def my_callback(value):
    switch.update_boolean(value)
    print GPIO.input(value)


GPIO.add_event_detect(MAGNET_GPIO, GPIO.BOTH, callback=my_callback)

def send_State(value):
    switch.update_boolean(value)

def main_thread():
    send_State(GPIO.input(MAGNET_GPIO))
    time.sleep(MQTT_PUBLISH_DELAY)

def main():
    while True:
        main_thread()


if name == 'main':
    main()
