import socket

serverName = "127.0.0.1"
serverPort = 8080

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(5)

clientSockets = []

while True:
    clientSocket, clientAddress = serverSocket.accept()
    clientSockets.append(clientSocket)

    data = clientSocket.recv(1024)
    if not data:
        clientSockets.remove(clientSocket)
        clientSocket.close()
        continue

    message = data.decode()

    for client in clientSockets:
        client.sendall(message.encode())

serverSocket.close()
