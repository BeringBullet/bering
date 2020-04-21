import time
from homie.device_temperature_humidity import Device_Temperature_Humidity

mqtt_settings = {
    "MQTT_BROKER": "192.168.86.30",
    "MQTT_PORT": 1883,
}


def on_message(client, userdata, message):
    print("message received ", message.payload)


def main():
    temp_hum = Device_Temperature_Humidity(
        device_id="t1", name="Temp", mqtt_settings=mqtt_settings)

    temp_hum.add_subscription("homie/t1/#", on_message)

    while True:
        time.sleep(2)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("Quitting.")
