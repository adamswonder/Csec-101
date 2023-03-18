import socket

ip = input("Enter IP address to scan: ")
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(0.1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port}: Open")
    s.close()