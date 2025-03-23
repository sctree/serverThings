import json
import http.client

# Define the server and port
HOST = 'localhost'
PORT = 8080

def send_floats(float_array):
    # Prepare the data to send
    data = {"floats": float_array}
    json_data = json.dumps(data)

    # Create an HTTP connection to the server
    connection = http.client.HTTPConnection(HOST, PORT)

    # Send the POST request with the JSON data
    headers = {'Content-Type': 'application/json'}
    connection.request('POST', '/', body=json_data, headers=headers)

    # Get the response from the server
    response = connection.getresponse()
    response_data = response.read().decode()

    # Close the connection
    connection.close()

    if response.status == 200:
        # Parse the JSON response and print it
        response_json = json.loads(response_data)
        print("Received from server:", response_json["floats"])
    else:
        print(f"Error {response.status}: {response_data}")

if __name__ == "__main__":
    float_array = [1.23, 4.56, 7.89]  # Example float array
    send_floats(float_array)
