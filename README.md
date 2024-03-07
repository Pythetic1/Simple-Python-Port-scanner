# Simple-Python-Port-scanner
Explore the Simple Port Scanner project! Learn to build a basic yet powerful port scanner with clear documentation. Perfect for beginners and those seeking to expand their cybersecurity skills.


# Documentation

## Port_Scaner_1

This script imports the `socket` module, which provides access to the BSD socket interface. These are communication endpoints that allow two processes to communicate with each other across a network or on a local machine.

`sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` This line creates a new object called `sock` from the `socket` module. We then specify to only use IPv4 `socket.AF_INET`. To instead do IPv6, we use `socket.AF_INET6`.

`socket.SOCK_STREAM` specifies we want to only use TCP. If we wanted to specifically do UDP, we would use `socket.SOCK_DGRAM`.

`connect_ex` is a non-blocking version of the `connect` method. It attempts to establish a connection to the specified address and returns an error code instead of blocking the program if it fails. If the connection is successful, it returns 0.

`result = sock.connect_ex(("192.168.0.250", 5000))` makes a variable called `result` that will use the object we created called `sock` to do a TCP request using IPv4 and then we use it to connect to a specified IP and Port. To change the port, we can manually do it or make a for loop with the port ranges and with a variable called `port`, then include the variable. Based on the result, if it is 0 it means the port is open, but anything else means the port is not accessible, so probably closed.

## Port_Scanner_2
`import socket`: This line imports the `socket` module, which provides access to BSD socket interfaces.
 
 `ip_address = input("Please enter the IP address you want to scan: ")`: This line prompts the user to input the IP address they want to scan and stores it in the variable `ip_address`.
 
 `port_range = input("Please specify the port range you want, for example 5000-5001: ")`: This line prompts the user to specify the port range they want to scan, for example, "5000-5001", and stores it in the variable `port_range`.
 
`port_range = port_range.split("-")`: This line splits the port range specified by the user into start and end ports and stores them as strings in a list.

`port_start = int(port_range[0])` and `port_end = int(port_range[1])`: These lines convert the start and end ports from strings to integers.

`for port in range(port_start, port_end):`: This line iterates through the specified port range, attempting to scan each port.

`sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`: This line creates a socket object for TCP connections.

`result = sock.connect_ex((ip_address, port))`: This line attempts to establish a connection to the IP address and port specified by the user and stores the result in the variable `result`.

`if result == 0:` and `else:`: These lines check if the connection was successful (port is open) or not (port is closed) and print the corresponding message.

`sock.close()`: This line closes the socket connection after scanning all ports in the specified range.
