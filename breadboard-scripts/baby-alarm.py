import RPi.GPIO as GPIO
import time 

PIR_PIN = 4
LED_PIN_LIST = [17, 27, 22]

dpath + "img" + time_of_capture + ".jpg"ef sound_alarm():
    counter = 0
    while counter < 5:
        for pin in LED_PIN_LIST:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(.5)
        for pin in LED_PIN_LIST:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(.5)
        counter += 1

def disable_alarm():
    for pin in LED_PIN_LIST:
        GPIO.output(pin, GPIO.LOW)

GPIO.setmode(GPIO.BCM)
for PIN in LED_PIN_LIST:
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, GPIO.LOW)

GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    time.sleep(0.1)
    print(GPIO.input(PIR_PIN))

    if GPIO.input(PIR_PIN) == 1:
        sound_alarm()

GPIO.cleanup()
