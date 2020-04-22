import RPi.GPIO as GPIO
import time

 
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
MAGNET_GPIO = 17



def my_callback(value):
    print GPIO.input(value)

GPIO.setup(MAGNET_GPIO, GPIO.IN) # GPIO Assign mode
GPIO.add_event_detect(MAGNET_GPIO, GPIO.BOTH, callback=my_callback)
while True:
    time.sleep(5)