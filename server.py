#import socket module
from socket import *
import os # In order to get the current working directory
import sys # In order to terminate the program

#Prepare a sever socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

#Fill in start
serverSocket.listen(1)
print('The server is ready to receive')


#parsing http request
while True:
        # Wait for client connections
    client_connection, client_address = serverSocket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)


        # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':
        filename = '/index.html'

    try:
        # fin = open('htdocs' + filename)
        # content = fin.read()
        with open('htdocs' + filename, 'rb') as fin:
            content = fin.read().decode('utf-8', 'ignore')
        
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:

        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    # Send HTTP response
    client_connection.sendall(response.encode())
    
    # # Send HTTP response
    # response = 'HTTP/1.0 200 OK\n\nHello World'
    # client_connection.sendall(response.encode())
    # client_connection.close()

    
    """ # Terima koneksi dari klien
    client_connection, client_address = serverSocket.accept()
    
    # Terima HTTP request dari klien
    request = client_connection.recv(1024)
    
    try:
        # Parse HTTP request
        request_parts = request.split(b'\r\n')
        request_line = request_parts[0].decode('utf-8')
        method, path, version = request_line.split()
        
        # Cari file yang diminta oleh klien
        file_path = os.getcwd() + path
        
        
        if os.path.isfile(file_path):
            # Jika file tersedia, baca isinya
            with open(file_path, 'rb') as file:
                content = file.read()
            
            # Buat HTTP response message
            response_line = b'HTTP/1.1 200 OK\r\n'
            response_header = b'Content-Type: text/html\r\n'
            response_body = content
        else:
            # Jika file tidak tersedia, kirim pesan 404 Not Found
            response_line = b'HTTP/1.1 404 Not Found\r\n'
            response_header = b'Content-Type: text/plain\r\n'
            response_body = b'404 Not Found'
        
        # Kirim HTTP response message ke klien
        response = response_line + response_header + b'\r\n' + response_body
        client_connection.sendall(response)
    
    except ValueError:
        # Jika permintaan HTTP tidak memiliki format yang benar, kirim pesan 400 Bad Request
        response_line = b'HTTP/1.1 400 Bad Request\r\n'
        response_header = b'Content-Type: text/plain\r\n'
        response_body = b'400 Bad Request'
        response = response_line + response_header + b'\r\n' + response_body
        client_connection.sendall(response) """
    
    # Tutup koneksi dengan klien
    client_connection.close()


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