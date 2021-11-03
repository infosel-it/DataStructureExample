import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print ('connecting', server_address)
sock.connect(server_address)

try:
    message = "Advanced Networks"
    print("Sending message ")
    sock.sendall(message.b)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print ('received', data)

finally:
    print('closing socket')
    sock.close()