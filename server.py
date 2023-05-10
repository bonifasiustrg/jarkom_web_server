from socket import *
import os # In order to get the current working directory
import sys # In order to terminate the program
import mimetypes # In order to determine the content type of the requested file

#Prepare a sever socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

#Fill in start
serverSocket.listen(1)
print('The server is ready to receive')

def not_found():
    content = '<html><body><h1>404 Not Found</h1></body></html>'
    return 'HTTP/1.0 404 Not Found\nContent-Type: text/html\n\n' + content

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

    # Check if the requested file exists
    file_path = 'htdocs' + filename
    if not os.path.isfile(file_path):
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
        client_connection.sendall(response.encode())
        client_connection.close()
        continue

    # Determine the content type of the requested file
    content_type, encoding = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = 'application/octet-stream'

    # If the requested file is an image, read and send the binary data
    if content_type.startswith('image/'):
        with open(file_path, 'rb') as f:
            file_data = f.read()
        response = 'HTTP/1.0 200 OK\nContent-Type: {}\n\n'.format(content_type).encode()
        response += file_data
        client_connection.sendall(response)
        client_connection.close()
        continue
    try:
        # fin = open('htdocs' + filename)
        # content = fin.read()
        with open('htdocs' + filename, 'rb') as fin:
            content = fin.read().decode('utf-8', 'ignore')

        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
        response = not_found()

    client_connection.sendall(response.encode())
    client_connection.close()
