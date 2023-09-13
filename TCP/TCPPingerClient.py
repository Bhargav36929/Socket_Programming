# TCPPingerClient.py
# Libraries required for socket & calculatinge RTT and it's Statistics
import socket
import time
import sys

# Create a TCP socket
# AF_INET for Address Family - IPv4 Network, SOCK_STREAM for TCP packets
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# As the server is listening the client request's for connection
clientSocket.connect(("127.0.0.1", 9003))

# Client will wait for 1sec if no response comes form server
clientSocket.settimeout(1)

# Getting input from user to send N packets
N = int(input("Enter no. of Packets: "))

# Some variables for calculation of RTT and it's Statistics
pktRetrans = 0
maxRTT = sys.maxsize*(-1)
minRTT = sys.maxsize
avgRTT = 0

for i in range(N):
   msg = f"ping {i+1}"

   # Start timestamp just before sending the packet
   stime = time.time()
   clientSocket.send(msg.encode())

   while True:
       try:
           # Response form server and ending timestamp  
           response = clientSocket.recv(1024)
           etime = time.time()

           # Calculating RTT and updating min max RTT
           diff = etime - stime
           maxRTT = max(maxRTT, diff)
           minRTT = min(minRTT, diff)
      
           # Summing all the RTT for avgerage at the end
           avgRTT += diff
          
           # Decoding and printing the response and it's RTT
           pkt = response.decode()
           print(f"{pkt}  {stime} -- {etime}  {round(diff, 6)}")
           break

       except socket.error as e:
           # Printing the Time out error and incrementing the packet retransmited variable
           print(f"Requested Time Out....Re-transmitting")
           pktRetrans += 1
          
           # Again giving the new start time as we are retransmitting
           stime = time.time()
           clientSocket.send(msg.encode())

clientSocket.close()

TotalpktTrans = pktRetrans + N
pktloss = pktRetrans / TotalpktTrans

# printing the RTT and it's Statistics
print(f"\nPacket Retransmitted: {(pktRetrans)}")
print(f"Average RTT: {round((avgRTT/N), 6)}")
print(f"Minimum RTT: {round(minRTT, 6)}")
print(f"Maximum RTT: {round(maxRTT, 6)}")
print(f"Packet loss: {round(pktloss*100, 2)}%")