from socket import *
from codecs import *

import numpy as np

serverPort = 50006
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)

print("Waiting for users...")

i = 0
vals = []
shadows = []
while i < 3:
    connectionSocket, clientAaddress = serverSocket.accept()
    print("Received from client " + str(clientAaddress))
    message = connectionSocket.recv(2048).decode()
    nums = message.split(",")
    
    vals.append(int(nums[0]))
    shadows.append(int(nums[1]))
    connectionSocket.close()
    i = i + 1
    
print("Received:")    
print(vals)
print(shadows)

A = np.array([[vals[0]**2, vals[0], 1],[vals[1]**2, vals[1], 1],[vals[2]**2,vals[2],1]])
Ainv = np.linalg.inv(A)

B = np.array([[shadows[0]],[shadows[1]],[shadows[2]]])

print("Result:")
result = np.matmul(Ainv, B).round().astype(int)
newA = result[0][0]
newB = result[1][0]
newC = result[2][0]
print("A: " + str(newA) + "\tB: " + str(newB) + "\tC: " + str(newC))