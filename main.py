from flask import Flask
import requests,os

app = Flask(__name__)

@app.route("/")
def index():
    ip = requests.get("https://api.ipify.org?format=json").json()
    return ip

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

