import paho.mqtt.client as mqtt
import threading
import time
import relay
from datetime import datetime
from homie.device_dimmer import Device_Dimmer

mqtt_settings = {
    'MQTT_BROKER': '192.168.86.30',
    'MQTT_PORT': 1883,
}

broker_address = "192.168.86.30"
clientName = "mainbase"
subscribers = ["relays"]
print("creating new instance")
client = mqtt.Client(clientName)  # create new instance

def on_message(client, userdata, message):
    print("message received ", message.payload)

def connect():
    print("connecting to broker")
    client.connect(broker_address)  # connect to broker

def subscribing():
    for x in subscribers:
        print("Subscribing to topic", x)
        client.subscribe(x)

def setup():
    client.on_message = on_message  # attach function to callback

def thread_function():
    client.loop_forever()

def sendMessage(msg):
    client.publish(clientName, str(msg))

def testmsg():
    now = datetime.now()
    msg = "Test msg sent on " + now.strftime("%Y-%m-%d %H:%M:%S")
    return msg

def main_thread():
    time.sleep(5)
    sendMessage(testmsg())

def main():

    #setup()
    #connect()
    #subscribing()

    #x = threading.Thread(target=thread_function)
    #x.start()
    #while True:
    #    main_thread()

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")
    
if __name__ == '__main__':
    main()
