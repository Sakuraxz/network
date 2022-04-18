from socket import *

serverName = '192.168.2.104'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifieMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifieMessage.decode())
clientSocket.close()