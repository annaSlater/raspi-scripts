import os
from flask import Flask

# initializes flask application
app = Flask(__name__, static_url_path="/home/pi/projects/pi-scripts/final-project/camera/", static_folder="/home/pi/projects/pi-scripts/final-project/camera/")


@app.route("/")
def index():
    return "hello from new server!"
@app.route("/check-movement")
def check_movement():
    photo_path = "/home/pi/projects/pi-scripts/final-project/camera/"
    log_path = "/home/pi/projects/pi-scripts/final-project/photo_logs.txt"
    if os.path.isfile(log_path):
        f = open(log_path, 'r')
        photos_list = f.readlines()
        f.close()
        return ("the number of photos is " + str(len(photos_list)) + " and the last photo taken was <img src=\"" + photo_path + str(photos_list[-1]) + "\">")
    
# runs application until stop singal 
app.run(host="0.0.0.0", port=8500)
