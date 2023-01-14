import RPi.GPIO as GPIO
from picamera import PiCamera
import time 
import os
import yagmail 

PIR_PIN = 4
LED_PIN_LIST = [17, 27, 22]

# set up email
password = ""
with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()
yag = yagmail.SMTP('aslater.raspi@gmail.com', password)

path = "/home/pi/projects/pi-scripts/final-project/camera/"
log_path = "/home/pi/projects/pi-scripts/final-project/photo_logs.txt"

GPIO.setmode(GPIO.BCM)

# set up pir
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# set up leds 
for PIN in LED_PIN_LIST:
    GPIO.setup(PIN, GPIO.OUT)

for PIN in LED_PIN_LIST:
    GPIO.output(PIN, GPIO.LOW)


def take_photo(path, time_of_capture, items_to_send):
    image_name = "img-" + str(time_of_capture) + ".jpg"
    f = open(log_path, 'a')
    f.write(image_name + "\n") 
    camera.capture(path + image_name)
    print("PHOTO TAKEN")
    items_to_send.append(path + image_name)

def send_email(items_to_send):
    yag.send(to="annakate.slater@gmail.com",
        subject="motion detected",
        contents="hello from the pir sensor and camera",
        attachments=items_to_send)
    print("sent the email!")
    items_to_send = [log_path]
    return items_to_send

# set up camera
camera = PiCamera()
camera.resolution = (1280, 720)
camera.rotation = 180
time.sleep(2)


# initialize log file
if not os.path.isfile(log_path):
    f = open(log_path, 'a')
    f.close()
else:
    os.remove(log_path)

 # previous_state = GPIO.input(PIR_PIN)
counter = 0
time_counter = 0
items_to_send = [log_path]
while True:
    current_state = GPIO.input(PIR_PIN)
    time.sleep(0.1)
    # every min send a photo 
    if time_counter == 600:
        if len(items_to_send) > 1:
            items_to_send = send_email(items_to_send)
        time_counter = 0
    if GPIO.input(PIR_PIN) == 1:
        counter += 1
        time_counter += 1
        if counter == 30:
            # get timestamp
            time_of_capture = time.time()
            # take photo
            take_photo(path, time_of_capture, items_to_send)
            # power on light
            for pin in LED_PIN_LIST:
                GPIO.output(pin, GPIO.HIGH)
            # reset counter
            counter = 0
    else:
        for pin in LED_PIN_LIST:
            GPIO.output(pin, GPIO.LOW)
        counter = 0
        time_counter += 1

GPIO.cleanup()
