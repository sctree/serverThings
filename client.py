import requests
import json
import time

SERVER_URL = "http://localhost:8000"

def send_number(number):
    # Send a number to server
    data = json.dumps({"number": number})

    start_time = time.time()
    response = requests.post(SERVER_URL, data=data)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Server response: {response.text} (Processed in {elapsed_time:.4f} seconds)")

def get_number():
    "# Request stored number from server"
    start_time = time.time()
    response = requests.get(SERVER_URL)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if response.status_code == 200:
        data = response.json()
        print(f"Stored number: {data['number']} (Processed in {elapsed_time:.4f} seconds)")
    else:
        print("Error retrieving number.")

if __name__ == "__main__":
    send_number(42)
    get_number()