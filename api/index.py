import json
import requests

def handler(request):
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return {
            "statusCode": 200,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps(response.json())
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
