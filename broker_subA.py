import socket

HOST = "127.0.0.1"
PORT = 8080

topic = input("Enter a topic to subscribe to: ")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))

clientSocket.sendall(("SUBSCRIBE " + topic + "\n").encode())

while True:
    data = clientSocket.recv(1024)
    if not data:
        break

    message = data.decode()

    if message == "SUBSCRIBE_CONFIRMATION_ACK":
        break

    print(message)

clientSocket.close()
