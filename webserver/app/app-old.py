from flask import Flask, render_template, send_file, make_response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from random import seed, randint
from datetime import datetime
import relay, sensor
import io

app = Flask(__name__)
def get_TemplateData():
    now = datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    relay1_value = relay.api_pin_value(23)
    relay2_value = relay.api_pin_value(24)
    relay3_value = relay.api_pin_value(25)

    templateData = {
        'title': "Bering bullet's Garage!",
        'time': timeString,
        'relay1': relay1_value,
        'relay2': relay2_value,
        'relay3': relay3_value
    }
    return templateData

@app.route("/")
def hello():
    templateData = get_TemplateData()
    return render_template('index.html', **templateData)


@app.route("/api/v1/ping/", methods=['GET'])
def api_status():
    return relay.api_status()


@app.route("/api/v1/gpio/<pin_number>/<action>")
def gpio_pin(pin_number, action):
    relay.gpio_pin(pin_number, action)
    templateData = templateData()
    return render_template('index.html', **templateData)


@app.route("/api/v1/gpio/status/<pin_number>")
def gpio_pin_status(pin_number):
    return relay.api_pin_value(pin_number)


@app.route("/api/v1/gpio/flip/<pin_number>")
def gpio_pin_flip(pin_number):
    relay.gpio_pin_flip(pin_number)


@app.route("/api/v1/gpio/status/", methods=['GET'])
def gpio_status():
    return relay.gpio_status()


@app.route("/api/v1/gpio/all-high/", methods=['POST'])
def gpio_all_high():
    return relay.gpio_all_high()


@app.route("/api/v1/gpio/all-low/", methods=['POST'])
def gpio_all_low():
    return relay.gpio_all_low()





# main route
@app.route("/sensors")
def index():
    templateData = sensor.sensor_data()
    return render_template('sensors.html', **templateData)


@app.route('/sensors', methods=['POST'])
def my_form_post():
    global numSamples
    global freqSamples
    global rangeTime
    rangeTime = int(request.form['rangeTime'])
    if (rangeTime < freqSamples):
        rangeTime = freqSamples + 1
    numSamples = rangeTime//freqSamples
    numMaxSamples = sensor.maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)

    templateData =  sensor.sensor_data()
    return render_template('sensors.html', **templateData)


@app.route('/plot/temp')
def plot_temp():
    times, temps, hums = sensor.getHistData(sensor.numSamples)
    ys = temps
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [°C]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    xs = range(sensor.numSamples)
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot/hum')
def plot_hum():
    times, temps, hums = sensor.getHistData(sensor.numSamples)
    ys = hums
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Humidity [%]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    xs = range(sensor.numSamples)
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == '__main__':
     app.run(debug=True, port=5000, host='0.0.0.0')
