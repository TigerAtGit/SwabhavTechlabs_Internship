from flask import Flask
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def hello():
    return "Welcome to my first WebApp" + str(datetime.now())
def greet():
    return "Hello Ji"
