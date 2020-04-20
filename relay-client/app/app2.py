#!/usr/bin/env python

import time
import relay
from homie.device_switch import Device_Switch

mqtt_settings = {
    "MQTT_BROKER": "192.168.86.30",
    "MQTT_PORT": 1883,
}


class Switch(Device_Switch):

    def __init__(
        self, device_id=None, gpio_pin=None, name=None, homie_settings=None, mqtt_settings=None
    ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)
        self.pin_number = gpio_pin
    
    def set_switch(self, onoff):
        relay.gpio_pin(self.pin_number, onoff)
        super().set_switch(onoff)


try:

    relay1 = Switch(device_id="relay1", gpio_pin=23, name="Relay 1", mqtt_settings=mqtt_settings)

    while True:
        time.sleep(5)
        #print("send ON")
        #relay1.update_switch("ON")
        #time.sleep(5)
        #print("send OFF")
        #relay1.update_switch("OFF")

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
    switch = None
