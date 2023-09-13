# TCPPingerConcurrentServer.py
# To create thread per client we require threading library
import socket
import threading

# Create a TCP socket
# AF_INET for Address Family - IPv4 Network, SOCK_STREAM for TCP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind(("127.0.0.1", 9003))

# Server listening for incoming connection
serverSocket.listen()

# Function to handel the each Client thread
def client(clientSocket, address):
   connected = True   
   while connected:
       # Receving and decoding the message form client
       message = clientSocket.recv(1024).decode()
       # Capitalize the message received form the client
       message = message.upper()

       # condition to break out form while loop
       if not message:
           connected = False

       # Sending back the modified message
       clientSocket.send(message.encode())

   # Closing the socket
   clientSocket.close()

try:
   while True:
       # for every client we have to accept the connection request
       clientSocket, address = serverSocket.accept()
       print(f"Connection with {address} has been established")
      
       # After accepting we create Thread for each client
       thread = threading.Thread(target=client, args=(clientSocket, address))
       thread.start()

       # Printing the No. of Threads that are acttive
       print(f"Active Threads {threading.active_count() - 1}")

except socket.error as e:
   print(e)

finally:
   serverSocket.close()