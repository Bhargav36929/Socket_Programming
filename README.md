# Socket Programming

- While testing first run Server then client.
- If generating packet loss at NIC then first implement it's command. Then after server and client.
- In case of concurrent server using the two instance of client both requesting to same server.

### PART-1: UDP Pinger
This client-server application operates on the UDP protocol, allowing message transfer without establishing a connection. The process is straightforward: the client sends a message, and the server responds with the same message converted to uppercase.
- Using a random library to generate the Artificial packet loss of 33%.
     - UDPPingerServer.py
     - UDPPIngerClient.py
- Removing the Artificial packet loss and implementing directly at NIC use the following command in the terminal
     - Run NIC's command at Server's terminal
     - UDPPingerModifiedServer.py
     - UDPPingerClient.py

```bash
sudo tc qdisc add dev eth0 root netem loss 33%

# Removing the packet loss
sudo tc qdisc del dev eth0 root netem loss 33%

# Change to different percentage
sudo tc qdisc change dev eth0 root netem loss 50%

# To change the internet interface replace 'eth0'
sudo tc qdisc change dev lo root netem loss 33%
```

### PART-2: TCP Pinger
The TCP protocol is connection-oriented, the client and server must first establish a connection before they can exchange data packets. To achieve this, the server uses 'listen' and 'accept' while the client sends connection request using 'connect'.
- Using a random library to generate the Artificial packet loss of 33%.
  - TCPPingerServer.py
  - TCPPnigerClient.py
- Removing the Artificial packet loss and implementing directly at NIC
  - Run NIC's command at Server's terminal
  - TCPPingerModifiedServer.py
  - TCPPingerModifiedClient.py
- Implementing the TCP Concurrent Server using Threading library
  - Run NIC's command at Server's terminal
  - TCPPingerConcurrentServer.py
  - TCPPingerModifiedClient.py
