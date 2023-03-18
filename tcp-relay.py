import socket

# Set up the listening socket
server_ip = '127.0.0.1'  # replace with the IP address of the server you want to replay to
server_port = 8080  # replace with the port number of the server you want to replay to
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

# Accept a connection from the client
print('Waiting for connection...')
client_socket, client_address = server_socket.accept()
print('Connection established:', client_address)

# Receive data from the client and replay it to the server
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print('Received data:', data)
    try:
        server_socket.sendall(data)
    except BrokenPipeError:
        print('Connection closed by client')
        break

# Clean up the sockets
client_socket.close()
server_socket.close()