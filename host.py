from socket import *
from codecs import *

i = 0 #number of clients handled
val = [6,2,5,7,9] # random values for x

def f(x):
	return (a*(x**2) + b*(x) + c)
    
def on_client(clientSocket,addr):
    print("Client " + str(addr) + " connected...")
    clientSocket.send((str(val[i]) + "," + str(f(val[i]))).encode()) # send x,f(x)
    clientSocket.close()
    print("Connection closed...")

serverPort = 50005
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)

print("Local Host Started")

# "Secret" Coefficients, only known by host
a = 17
b = 4
c = 25

# print coefficients and value/shadow pairs for debug
print("A: " + str(a) + "\tB: " + str(b) + "\tC: " + str(c))

print("Value 1: " + str(val[0]) + "\tShadow 1: " + str(f(val[0])))
print("Value 2: " + str(val[1]) + "\tShadow 2: " + str(f(val[1])))
print("Value 3: " + str(val[2]) + "\tShadow 3: " + str(f(val[2])))
print("Value 4: " + str(val[3]) + "\tShadow 4: " + str(f(val[3])))
print("Value 5: " + str(val[4]) + "\tShadow 5: " + str(f(val[4])))


while i < 5:
    clientSocket, addr = serverSocket.accept()
    on_client(clientSocket,addr)
    i = i + 1
serverSocket.close()
