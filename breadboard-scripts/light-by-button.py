import RPi.GPIO as GPIO
import time 

BUTTON_PIN = 26
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    # this is here to reduce cpu usage 
    time.sleep(.01)
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif GPIO.input(BUTTON_PIN) == GPIO.LOW:
        GPIO.output(LED_PIN, GPIO.LOW)
    else:
        continue;
GPIO.cleanup()
exit()

