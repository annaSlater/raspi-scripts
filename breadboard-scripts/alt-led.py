import RPi.GPIO as GPIO
import time 

BUTTON_PIN = 26
RED_LED_PIN = 17
BLUE_LED_PIN = 27
GREEN_LED_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

GPIO.output(RED_LED_PIN, GPIO.LOW)
GPIO.output(BLUE_LED_PIN, GPIO.LOW)
GPIO.output(GREEN_LED_PIN, GPIO.LOW)

previous_button_state = GPIO.input(BUTTON_PIN);
counter = 0
while True:
    time.sleep(.01)
    if previous_button_state != GPIO.input(BUTTON_PIN):
        if counter == 0:
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            previous_button_state = GPIO.input(BUTTON_PIN);
            counter++
        elif counter == 1:
            GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
            previous_button_state = GPIO.input(BUTTON_PIN);
            counter++
        else: 
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
            previous_button_state = GPIO.input(BUTTON_PIN);
            counter = 0

GPIO.cleanup()
exit()

