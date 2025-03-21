from http.server import BaseHTTPRequestHandler, HTTPServer
import json


stored_number = 0

class NumberHandler(BaseHTTPRequestHandler):
    # Handle a GET request to send the stored number
    def do_GET(self):
        global stored_number
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"number": stored_number}
        self.wfile.write(json.dumps(response).encode())

    # Handle POST request to receive a number and store it
    def do_POST(self):
        global stored_number
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        received_data = json.loads(post_data)

        if "number" in received_data:
            stored_number = received_data["number"]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Number stored successfully!")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid data format")

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, NumberHandler)
    print("Server running in port 8000")
    httpd.serve_forever()
