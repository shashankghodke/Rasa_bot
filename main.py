import requests

def send_message(message):
    url = "http://localhost:5005/webhooks/rest/webhook"
    data = {"sender": "test_user", "message": message}
    response = requests.post(url, json=data)
    return response.json()

if __name__ == "__main__":
    while True:
        message = input("You: ")
        response = send_message(message)
        for res in response:
            print(f"Bot: {res['text']}")
