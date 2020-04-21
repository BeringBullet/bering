from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["USERINFO"] = {
    "broker_address": "192.168.86.30",
    "clientname": "GD1",
    "MQTT_TOPIC_HUMIDITY": "garage/1/humidity",
    "MQTT_TOPIC_TEMPERATURE": "garage/1/temperature",
    "MQTT_TOPIC_STATE": "garage/1/status",
    "MQTT_PUBLISH_DELAY": "10",
    "MQTT_CLIENT_ID": "dht22"
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)
