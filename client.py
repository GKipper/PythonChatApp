import socket
from threading import Thread

def receiveMsg(client_socket):
    while True:
        try:
            data = client_socket.recv(514).decode()  # receive response
            print(data)
        except Exception as e:
            break

def client_program():
    host = 'localhost'
    port = 5500  # socket server port number

    
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input("Name: ")  # take input

    Thread(target=receiveMsg, args=(client_socket,)).start()

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message

        message = input()  # again take input
    else:
        client_socket.send(message.encode())
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()