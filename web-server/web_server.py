from flask import Flask
from views import views

# initializes flask application
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

# runs application until stop singal 
app.run(host="0.0.0.0", port=8500)
