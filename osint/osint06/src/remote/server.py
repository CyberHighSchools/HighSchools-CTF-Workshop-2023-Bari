import socket
import os


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(20)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = os.environ.get('PORT', 8888)
FLAG = os.environ.get('FLAG', 'flag{...}')
sock.bind(('', PORT))

sock.listen(5)

try:
    while True:
        newSocket, address = sock.accept()
        print("Connected from", address)
        
        newSocket.send(FLAG.encode())

        newSocket.close()
        print("Disconnected from", address)
finally:
    sock.close()