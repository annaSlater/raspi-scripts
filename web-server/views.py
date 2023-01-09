from flask import Blueprint, render_template
import RPi.GPIO as GPIO

views = Blueprint(__name__, "views")

BUTTON_PIN = 26
LED_PINS = [17, 27, 22]
# initializes GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

for x in LED_PINS:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.LOW)

@views.route("/")
def home():
    return render_template("index.html")
@views.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        pressed = "True"
    else:
        pressed = "False"
    return render_template("push_button.html", state=pressed)

@views.route("/led/<int:led_pin>/state/<int:led_state>")
def change_led_state(led_pin, led_state):
    if not(led_pin in LED_PINS):
        result = "Not valid pin"
    if led_state == 1:
        GPIO.output(led_pin, GPIO.HIGH)
        result = "successfully powered on"
    elif led_state == 0:
        GPIO.output(led_pin, GPIO.LOW)
        result = "successfully powered off"
    else:
        result = "invalid state change"
    return render_template("change_led_state.html", result=result, led_pin=led_pin, led_state=led_state)
