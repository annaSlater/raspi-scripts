import RPi.GPIO as GPIO
import time 

LED_PIN_LIST = [17, 27, 22]
BUTTON_PIN = 26

def power_on_led(pin_num):
    GPIO.output(pin_num, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)

for PIN in LED_PIN_LIST:
    GPIO.setup(PIN, GPIO.OUT)

GPIO.setup(BUTTON_PIN, GPIO.IN)

for PIN in LED_PIN_LIST:
    GPIO.output(PIN, GPIO.LOW)

previous_button_state = GPIO.input(BUTTON_PIN);
counter = 0
while True:
    time.sleep(.01)
    button_state = GPIO.input(BUTTON_PIN)
    if previous_button_state != button_state:
        previous_button_state = button_state
        if button_state == GPIO.HIGH:
            if counter == 0:
                power_on_led(LED_PIN_LIST[counter])
                counter+=1
            elif counter == 1:
                power_on_led(LED_PIN_LIST[counter])
                previous_button_state = GPIO.input(BUTTON_PIN);
                counter+=1
            elif counter == 2: 
                power_on_led(LED_PIN_LIST[counter])
                previous_button_state = GPIO.input(BUTTON_PIN);
                counter += 1
            else:
                for PIN in LED_PIN_LIST:
                    GPIO.output(PIN, GPIO.LOW)
                counter = 0
GPIO.cleanup()
exit()

