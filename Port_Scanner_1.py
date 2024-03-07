"""
This is a simple Python port scanner. In this example, we use a fixed IP address of 192.168.0.250 and a fixed port of 5000

"""

import socket  # BSD socket interface

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock is our variable from the socket module, socket class
# socket.AF_INET specifies the address family (IPv4)
# socket.SOCK_STREAM specifies the socket type (stream = two-way communication between endpoints)

result = sock.connect_ex(("192.168.0.250", 5000))
# This sets up a remote connection using our sock object from the socket module,
# specifying to scan the IP address and port number

if result == 0:
    print("Port 5000 is open")
else:
    print("Port 5000 is closed")
