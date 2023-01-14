import time
from picamera import PiCamera
import os

path = "/home/pi/projects/pi-scripts/series-camera" 
if not os.path.exists(path):
    os.mkdir(path)

camera = PiCamera()
camera.resolution = (1280, 720)
camera.rotation = 180
time.sleep(2)

counter = 1
while True:
    file_name = path + "/photo_" + str(counter) + ".jpg"
    print(file_name)
    camera.capture(file_name)
    counter += 1
    time.sleep(5)
