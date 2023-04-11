from socket import *
from codecs import *

hostName = "localhost"
hostPort = 50005

tpPort = 50006

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((hostName, hostPort))

message = clientSocket.recv(2048) #receive x,f(x) from local host
print(message.decode())
clientSocket.close()

trigger = input("Send to Third Party? [y/n]: ")
if (trigger == "y"):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((hostName,tpPort))
    clientSocket.send(message)
    clientSocket.close()