import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the content length and parse the data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Parse the JSON data
        try:
            data = json.loads(post_data)
            float_array = data.get("floats", [])

            # Modify the float array (e.g., add 1.0 to each element)
            modified_array = [x + 1.0 for x in float_array]

            # Send back the modified array in JSON format
            response_data = json.dumps({"floats": modified_array})
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response_data.encode())
            print("Received array:", float_array)
            print("Sent back modified array:", modified_array)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
