from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    ip = requests.get("https://api.ipify.org?format=json").json()
    return ip

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
