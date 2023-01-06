import RPi.GPIO as GPIO
# takes input from the user and casts it to a string 

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
print("Enter 1 or 0")

while True:

    state = int(input(":"))
    if state == 0:
      GPIO.output(LED_PIN, GPIO.LOW)
    elif state == 1:
      GPIO.output(LED_PIN, GPIO.HIGH)
    else:
      print("i;nvalid input")
      break;

GPIO.cleanup()
exit 

