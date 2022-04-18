from socket import *

serverName = '192.168.2.104'
serverPort = 12010
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence:')
clientSocket.send(message.encode())
modifieMessage = clientSocket.recv(1024)
print(modifieMessage.decode())
clientSocket.close()