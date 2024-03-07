# Simple-Python-Port-scanner
Explore the Simple Port Scanner project! Learn to build a basic yet powerful port scanner with clear documentation. Perfect for beginners and those seeking to expand their cybersecurity skills.


# Documentation

## Port_Scaner_1

This script imports the `socket` module, which provides access to the BSD socket interface. These are communication endpoints that allow two processes to communicate with each other across a network or on a local machine.

`sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` This line creates a new object called `sock` from the `socket` module. We then specify to only use IPv4 `socket.AF_INET`. To instead do IPv6, we use `socket.AF_INET6`.

`socket.SOCK_STREAM` specifies we want to only use TCP. If we wanted to specifically do UDP, we would use `socket.SOCK_DGRAM`.

`connect_ex` is a non-blocking version of the `connect` method. It attempts to establish a connection to the specified address and returns an error code instead of blocking the program if it fails. If the connection is successful, it returns 0.

`result = sock.connect_ex(("192.168.0.250", 5000))` makes a variable called `result` that will use the object we created called `sock` to do a TCP request using IPv4 and then we use it to connect to a specified IP and Port. To change the port, we can manually do it or make a for loop with the port ranges and with a variable called `port`, then include the variable. Based on the result, if it is 0 it means the port is open, but anything else means the port is not accessible, so probably closed.
