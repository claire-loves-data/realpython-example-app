from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "I made this during Martin's nap"