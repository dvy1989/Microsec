from socket import socket, SOCK_STREAM, AF_INET
import sys

if __name__ == "__main__":
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("localhost", 2999))
    # Name of script is nor needed
    message = " ".join(sys.argv[1:])
    print(message)
    try:
        client.sendall(message.encode())
        connected = True
        while connected:
            response = client.recv(1024)
            if len(response) > 0:
               print(response)
            else:
               # If server closes connection, then stop the app
               connected = False
    finally:
        client.close()
