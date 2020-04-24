import Adafruit_DHT
import time
from homie.device_temperature_humidity import Device_Temperature_Humidity
import paho.mqtt.client as mqtt  # import the client1

mqtt_settings = {
    "MQTT_BROKER": "192.168.86.30",
    "MQTT_PORT": 1883,
}

deviceID = "gs1"
MQTT_PUBLISH_DELAY = 60
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

temp_hum = Device_Temperature_Humidity(
    device_id=deviceID, name="Temp Hum", mqtt_settings=mqtt_settings)


def get_sensor_data():
    humidity, temperatureC = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temperatureF = (temperatureC * 9.0 / 5.0) + 32.0

    temp_hum.update_temperature(temperatureF)
    temp_hum.update_humidity(humidity)


def publish_homeassistant():
    hass_config = f'homeassistant/sensor/{deviceID}/config'
    hass_payload = f'{{"name": "Temp Hum","state_topic": "homie/gs1/status/temperature"}}'

    client = mqtt.Client(deviceID)  # create new instance
    client.connect("192.168.86.30")  # connect to broker
    client.publish(hass_config, hass_payload)  # publish

def main_thread():
    time.sleep(MQTT_PUBLISH_DELAY)
    get_sensor_data()

while True:
    publish_homeassistant()
    main_thread()


if __name__ == '__main__':
    main()
