import serial
import time
import struct  # Used to pack float data into binary format

# Open serial port (adjust the port name as needed)
ser = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=1)

def send_floats(float_array):
    """Send an array of floats over UART."""
    data = struct.pack(f"{len(float_array)}f", *float_array)  # Convert floats to binary
    ser.write(data)  # Send data over UART
    print(f"Sent: {float_array}")

# Example: Sending an array of floats every 2 seconds
while True:
    send_floats([1.23, 4.56, 7.89])  # Example float array
    time.sleep(2)
