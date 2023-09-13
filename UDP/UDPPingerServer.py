# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
import socket

# Create a UDP socket
# AF_INET for Address Family - IPv4 Network, SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('127.0.0.1', 7000))

while True:
   # Generate a random number between 0 to 11 (both included)
   rand = random.randint(0, 11)
   # Receive the client packet along with the address it is coming from
   message, address = serverSocket.recvfrom(1024)
  
   # Breaking out form the loop if no message received
   if not message:
      break

   # Capitalize the message from the client
   message = message.upper()
  
   # Creating Artificial Packet loss
   if rand < 4:
      continue

   # Otherwise, the server responds
   serverSocket.sendto(message, address)

serverSocket.close()