import socket
from threading import Thread
from user import User

HOST = 'localhost'
PORT = 5500
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER = 514
clients = []

def broadcast(msg, client):
    for user in clients:
        if client != user:
            user.conn.send(f"{client.name}: {msg}".encode())
            #SERVER.send(f"{client.name}: {msg}".encode())

def communication(client):
    run = True
    try:
        while run:
            msg = client.conn.recv(514).decode()
            if msg == 'bye':
                broadcast(f"{client.name} has been disconnected!", client)
                run = False
                client.conn.close()
                clients.remove(client)
                break
            else:
                broadcast(msg, client)
                #print(f"{client.name}: {msg}")

    except Exception as e:
        print("[ERROR]", e)
        #SERVER.close()

def acceptClients():
    while True:
        try:
            SERVER.bind((HOST, PORT))  # connect to the server
            break
        except Exception as e:
            pass

    print('waiting connection!')
    # configure how many client the server can listen simultaneously
    SERVER.listen(5)

    while True:
        try:
            conn, address = SERVER.accept()  # accept new connection

            name = conn.recv(514).decode()
            print(f"{name} is connected!")
            client = User(name, conn, address)
            clients.append(client)
            Thread(target=communication, args=(client,)).start()
        except Exception as e:
            print("[ERROR]", e)
            SERVER.close()


if __name__ == '__main__':

    TacceptClients = Thread(target=acceptClients)

    TacceptClients.start()
    TacceptClients.join()

    SERVER.close()