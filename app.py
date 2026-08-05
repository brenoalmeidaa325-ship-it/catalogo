from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return str(os.listdir("."))

if __name__ == "__main__":
    app.run()
