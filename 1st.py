import socket

# Define server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # The same port the server is listening on

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send some data to the server
message = "Hello, server!"
client_socket.sendall(message.encode())

# Receive the response from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# Close the connection
client_socket.close()