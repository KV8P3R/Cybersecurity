import socket

target = "example.com"
port = 80

s = socket.socket()

result = s.connect_ex((target, port))

if result == 0:
    print("Port is open")
else:
    print("Port is closed")

s.close()
