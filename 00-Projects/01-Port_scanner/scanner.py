import socket

target = "scanme.nmap.org"

for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.55)
    result = s.connect_ex((target,port))

    if result == 0:
        print("Port", port, "is open")

s.close()
