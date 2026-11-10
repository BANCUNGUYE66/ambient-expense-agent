import requests

url = "http://127.0.0.1:8080/run"
payload = {
    "message": "Test expense claim: $450 for software subscription"
}
headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(response.json())
except Exception as e:
    print(f"Error connecting to agent server: {e}")