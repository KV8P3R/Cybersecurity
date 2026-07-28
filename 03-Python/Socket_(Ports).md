socket – Networking & Port Scanning
Used to connect to ports and network servers.

Code:

import socket

s = socket.socket()
result = s.connect_ex(("192.168.1.10", 80))  # Returns 0 if the port is open
if result == 0:
    print("Port 80 is open")
s.close()
else:
    print("Port 80 is closed")
subprocess – Running System Commands
