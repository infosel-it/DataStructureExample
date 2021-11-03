import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)

print("starting up on address",server_address)
sock.bind(server_address)

sock.listen()

while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()
try:
        print ('connection from', client_address)
        while True:
            data = connection.recv(16)
            print (sys.stderr, 'received "%s"' % data)
            if data:
                print (sys.stderr, 'sending data back to the client')
                connection.sendall(data)
            else:
                print (sys.stderr, 'no more data from', client_address)
                break
finally:
    connection.close();