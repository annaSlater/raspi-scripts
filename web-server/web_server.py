from flask import Flask
from views import views

# initializes flask application
app = Flask(__name__)

@app.route("/")
def index():
    return "server is up!"

# runs application until stop singal 
app.run(host="0.0.0.0", port=8500)
