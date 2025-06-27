import requests

url = "http://localhost:5005/webhooks/rest/webhook"
data = {"sender": "user", "message": "Tell me about job prospects in data science"}

try:
    response = requests.post(url, json=data, timeout=5)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print("Error:", e)
