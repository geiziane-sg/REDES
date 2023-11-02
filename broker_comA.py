import socket

serverName = "127.0.0.1"
serverPort = 8080

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

command = "LIST"  # O comando LIST para obter a lista de tópicos e assinantes

clientSocket.sendall(("COMMAND " + command + "\n").encode())

data = clientSocket.recv(1024)

if not data:
    clientSocket.close()

message = data.decode()

print(message)

clientSocket.close()