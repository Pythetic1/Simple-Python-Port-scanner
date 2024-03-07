# Simple-Python-Port-scanner
Explore the Simple Port Scanner project! Learn to build a basic yet powerful port scanner with clear documentation. Perfect for beginners and those seeking to expand their cybersecurity skills.


# Instructions

## Port_Scaner_1

This script utilizes the socket module, providing access to the BSD socket interface. These interfaces facilitate communication between processes across networks or locally.

The line sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) instantiates a new object called sock from the socket module. We specify IPv4 communication with socket.AF_INET. To use IPv6, we would employ socket.AF_INET6.

socket.SOCK_STREAM indicates TCP usage exclusively. For UDP, we would use socket.SOCK_DGRAM.

connect_ex is a non-blocking version of connect, attempting connection establishment to a given address and returning an error code upon failure, without blocking the program. A successful connection yields a return value of 0.

result = sock.connect_ex(("192.168.0.250", 5000)) assigns the variable result, leveraging the sock object for a TCP request over IPv4, connecting to the specified IP and port. To adjust the port, one can manually modify it or employ a loop with port ranges using a variable. A result of 0 indicates an open port; any other value suggests inaccessibility, typically indicating closure.
