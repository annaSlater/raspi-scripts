import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)

# set the output for pin 17 to be output 
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.HIGH)

# waits 1 second before powering off
time.sleep(1)
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(1)
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(1)

for i in range(10):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(.5)

GPIO.cleanup()
