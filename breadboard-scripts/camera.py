from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1280, 720)
camera.rotation = 180
time.sleep(2)

# file_name = "/home/pi/projects/pi-scripts/camera/img.jpg"
# camera.capture(file_name)

file_name = "/home/pi/projects/pi-scripts/camera/video.h264"
camera.start_recording(file_name)
camera.wait_recording(10)
camera.stop_recording()

print("done")
