import socket

HOST = "127.0.0.1"
PORT = 8080

topic = input("Enter the topic to publish to: ")
message = input("Enter the message to publish: ")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))

clientSocket.sendall(("PUBLISH " + topic + " " + message + "\n").encode())

data = clientSocket.recv(1024)

clientSocket.close()

print(f"Message published to topic: {topic}")
