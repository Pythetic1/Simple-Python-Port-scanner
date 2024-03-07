This script imports socket which is a module that provides access to the <mark style="background: #ABF7F7A6;">BSD socket interface</mark>, these are communication endpoints that allow two processes to communicate with each other across a network or on a local machine.

`sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` This line creates a new object called sock from socket, we then <mark style="background: #ABF7F7A6;">specify to only use IPV4 </mark>`socket.AF_INET`. to instead do IPV6, we do `socket.AF_INET6`

`socket.SOCK_STREAM` specifies we want to <mark style="background: #ABF7F7A6;">only use TCP</mark>.
if we wanted to <mark style="background: #ABF7F7A6;">specifically do UDP</mark> we would do `socket.SOCK_DGRAM`

`connect_ex` is a non-blocking version of the `connect` method. It attempts to establish a connection to the specified address and returns an error code instead of blocking the program if it fails. If the connection is successful, it returns 0.

`result = sock.connect_ex(("192.168.0.250", 5000))` makes a variable called result that will use the object we created called sock to do a TCP request using IPV4 and then we use it to connect to a specified IP and Port, to change the port we can manually do it or make a for loop with the port ranges and with a variable called port and then include the variable. based of the result, if it is 0 it means the port is open but anything else means port is not accessible so probably closed.
