#import socket module
from socket import *
import sys # In order to terminate the program

#Prepare a sever socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

#Fill in start
serverSocket.listen(1)
print('The server is ready to receive')

#while yanh templete
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

#while yang dikerjakan
""" #Fill in end
while True: 
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  #Fill in start #Fill in end
    
    try:
        message = #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):     
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
    #Send response message forfile not found
    #Fill in start
    #Fill in end
    #Close client socket
    #Fill in start
    #Fill in end



serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding
data """