import RPi.GPIO as GPIO
import time

VALID_BCM_PIN_NUMBERS = [17, 23, 24, 25, 27]
VALID_LIGHT_PIN_NUMBERS = [23, 24, 25]
VALID_HIGH_VALUES = [1, '1', 'OFF']
VALID_LOW_VALUES = [0, '0', 'ON']
PIN_NAMES = {'17': 'Garoge door 1', '23': 'Shop light 1',
             '24': 'Shop light 2', '25': 'Shop light 3', '27': 'Garoge door 2'}

GPIO.setmode(GPIO.BCM)
GPIO.setup(VALID_BCM_PIN_NUMBERS, GPIO.OUT)
GPIO.output(VALID_BCM_PIN_NUMBERS, GPIO.HIGH)

def pin_status(pin_number):
    if pin_number in VALID_BCM_PIN_NUMBERS:
        value = GPIO.input(pin_number)
        data = {'pin_number': pin_number,
                'pin_name': PIN_NAMES[str(pin_number)],
                'value': value,
                'status': 'SUCCESS',
                'error': None}
    else:
        data = {'status': 'ERROR',
                'error': 'Invalid pin number.'}
    return data


def pin_update(pin_number, value):
    if pin_number in VALID_BCM_PIN_NUMBERS:
        GPIO.output(pin_number, value)
        new_value = GPIO.input(pin_number)
        data = {'status': 'SUCCESS',
                'error': None,
                'pin_number': pin_number,
                'pin_name': PIN_NAMES[str(pin_number)],
                'new_value': new_value}
    else:
        data = {'status': 'ERROR',
                'error': 'Invalid pin number or value.'}
    return data


def api_status():
    if request.method == 'GET':
        data = {'api_name': 'RPi GPIO API',
                'version': '1.0',
                'status': 'SUCCESS',
                'response': 'pong'}
        return jsonify(data)


def api_pin_value(pin_number):
    return GPIO.input(pin_number)

def gpio_pin(pin_number, action):
    pin_number = int(pin_number)
    value = action
    if value in VALID_HIGH_VALUES:
        data = pin_update(pin_number, 1)
    elif value in VALID_LOW_VALUES:
        data = pin_update(pin_number, 0)
    else:
        data = {'status': 'ERROR',
                'error': 'Invalid value.'}
    #return jsonify(data)

def gpio_pin_flip(pin_number):
    pin_number = int(pin_number)
    data = pin_update(pin_number, 0)
    time.sleep(1)
    data = pin_update(pin_number, 1)
    return True

def gpio_status():
    data_list = []
    for pin in VALID_BCM_PIN_NUMBERS:
        data_list.append(pin_status(pin))

    data = {'data': data_list}
    return jsonify(data)

def gpio_all_high():
    data_list = []
    for pin in VALID_LIGHT_PIN_NUMBERS:
        data_list.append(pin_update(pin, 1))

    data = {'data': data_list}
    return jsonify(data)

def gpio_all_low():
    data_list = []
    for pin in VALID_LIGHT_PIN_NUMBERS:
        data_list.append(pin_update(pin, 0))

    data = {'data': data_list}
    return jsonify(data)

