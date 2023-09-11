# TCPPingerModifiedServer.py
import socket


# Create a TCP socket
# AF_INET for Address Family - IPv4 Network, SOCK_STREAM for TCP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind(('127.0.0.1', 9003))


# Server listening for incoming connection
serverSocket.listen()
# Server accepts the incoming connection along with address it is coming form
clientSocket, address = serverSocket.accept()
print(f"Connection with {address} has been established")


try:
   while True:
       # Receiving client message
       msg = clientSocket.recv(1024)


       # If no message is there then breaking out form loop
       if not msg:
           break


       # Decoding and Capitalize the message from the client
       msg = msg.decode().upper()


       # Sending the Capitalize message to the client
       clientSocket.send(msg.encode())


finally:
   serverSocket.close()