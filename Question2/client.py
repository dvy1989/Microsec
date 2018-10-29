from socket import socket, SOCK_STREAM, AF_INET

if __name__ == "__main__":
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("localhost", 2999))
    message = "https://en.wikipedia.org/wiki/Finland Finland"
    try:
        client.sendall(message.encode())
        connected = True
        while connected:
            response = client.recv(1024)
            if len(response) > 0:
               print(response)
            else:
               connected = False
    finally:
        client.close()
