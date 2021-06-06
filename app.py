from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/<selector>/<temperature>')
def fahrenheit_to_celsius(selector='', temperature='0.0'):
    converted_temperature = 0
    converted_unit = ''
    if selector.upper() == 'C':  # Convert from Celsius to Fahrenheit
        converted_temperature = float(temperature) * 9.0 / 5 + 32
        converted_unit = 'F'
    elif selector.upper() == 'F':  # Convert from Fahrenheit to Celsius
        converted_temperature = 5 / 9 * (float(temperature) - 32)
        converted_unit = 'C'
    return "{:.2f} {} is {:.2f} {}"\
        .format(float(temperature), selector.upper(), converted_temperature, converted_unit)


if __name__ == '__main__':
    app.run()
