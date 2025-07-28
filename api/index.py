# api/index.py
import json
import requests

def handler(request):
    response = requests.get("https://api.ipify.org?format=json")
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps(response.json())
    }
