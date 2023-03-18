import socket
import datetime

# Define the IP address and port number to bind to
HOST = '192.168.100.27'  # Listen on all available network interfaces
PORT = 22  # Use port 22, the default SSH port

# Create the socket object and bind it to the IP address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(1)

# Create a file to log the activity to
log_file = open('honeypot.log', 'w')

# Accept incoming connections and log any activity to the file
while True:
    # Wait for a connection
    client_socket, address = server_socket.accept()

    # Log the connection information to the file
    log_file.write(f'Connection from {address[0]}:{address[1]} at {datetime.datetime.now()}\n')
    log_file.flush()

    # Receive data from the client and log it to the file
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            log_file.write(data)
            log_file.flush()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the client socket
        client_socket.close()

# Close the log file
log_file.close()