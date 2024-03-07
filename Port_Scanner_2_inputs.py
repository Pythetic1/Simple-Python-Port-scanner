import socket

# Ask the user to input the IP address they want to scan
ip_address = input("Please enter the IP address you want to scan: ")

# Ask the user to specify the port range they want to scan
port_range = input("Please specify the port range you want, for example 5000-5001: ")

# Split the port range into start and end ports based on a dash
port_range = port_range.split("-")

# Convert the start and end ports to integers
port_start = int(port_range[0])
port_end = int(port_range[1])

# Iterate through the specified port range
for port in range(port_start, port_end):

    # Create a socket object for TCP connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Attempt to establish a connection to the IP address and port
    result = sock.connect_ex((ip_address, port))

    # Check if the connection was successful (port is open)
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")

    # Close the socket connection
    sock.close()
