import RPi.GPIO as GPIO
from flask import Flask

BUTTON_PIN = 26
LED_PINS = [17, 27, 22]

# initializes flask application
app = Flask(__name__)

# initializes GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

for x in LED_PINS:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.LOW)

# create some routes 
@app.route("/")
def index():
    return "Hello from flask"

@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "button is pressed"
    else:
        return "button is not pressed"

@app.route("/led/<int:led_pin>/state/<int:led_state>")
def change_led_state(led_pin, led_state):
    if not(led_pin in LED_PINS):
        return "Not valid pin"
    if led_state == 1:
        GPIO.output(led_pin, GPIO.HIGH)
        return "successfully powered on"
    elif led_state == 0:
        GPIO.output(led_pin, GPIO.LOW)
        return "successfully powered off"
    else:
        return "invalid state change"

# runs application until stop singal 
app.run(host="0.0.0.0", port=8500)

