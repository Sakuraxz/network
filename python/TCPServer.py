from socket import *

serverPort = 12010
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
