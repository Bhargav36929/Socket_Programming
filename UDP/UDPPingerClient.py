# UDPPingerClient.py
# Importing the required libraries. Time for timestamping and sys for min max values
import socket
import time
import sys


# Create a UDP socket
# AF_INET for Address Family - IPv4 Network, SOCK_DGRAM for UDP packets
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Creating packet which will sent for N(user defined) times
message = "ping"
N = int(input("Enter the no. of packets: "))


# Encoding the message in bytes
message = message.encode()


# setting timeout for client so that it doesn't wait for infinite time
clientSocket.settimeout(1)


# Variables for Statistics for RTT
maxRTT = sys.maxsize*-1
minRTT = sys.maxsize
avgRTT = 0
pktloss = 0


for i in range(N):   
   try:
       # Creating the timestamp before sending & after receiving the packet using time library
       stime = time.time()
       # Sending message to server with it's address and port
       clientSocket.sendto(message, ('127.0.0.1', 7000))
       # Receiving the client packet along with the address it is coming from
       response, address = clientSocket.recvfrom(1024)
       etime = time.time()


       # Calculation of RTT and updating minRTT & maxRTT
       diff = etime - stime
       maxRTT = max(maxRTT, diff)
       minRTT = min(minRTT, diff)
      
       # Used for Calculation of AvgRTT at the end
       avgRTT += diff
      
       # First decoding the message received then printing
       response = response.decode()
       print(f'{response} {i+1}  {stime} -- {etime}  {round((diff), 6)}')


   except TimeoutError:
       # Handling the Timeout Error
       print("Request timed out")
       pktloss += 1
       continue


# Finally after N packets are sent & receive the client Socket is closed
clientSocket.close()


# Printing the RTT Statistics
print(f"\nMax RTT: {round((maxRTT), 6)}")
print(f"Min RTT: {round((minRTT), 6)}")
print(f"Average RTT: {round((avgRTT/N), 6)}")
print(f"Packet loss: {round(((pktloss/N)*100), 2)}%")