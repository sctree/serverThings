import serial
import struct

# Open serial port (adjust the port name as needed)
ser = serial.Serial('/dev/ttyUSB1', baudrate=115200, timeout=1)

def receive_floats(num_floats):
    """Receive an array of floats over UART."""
    data = ser.read(num_floats * 4)  # Read expected byte size (4 bytes per float)
    if len(data) == num_floats * 4:
        float_array = struct.unpack(f"{num_floats}f", data)  # Convert binary to floats
        print(f"Received: {float_array}")

# Continuously listen for incoming data
while True:
    receive_floats(3)  # Expecting 3 floats
