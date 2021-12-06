import socket
import os
from _thread import *
import json

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

userNames = {}


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        # data = data.decode('utf-8')
        data = json.loads(data.decode('utf-8'))

        if not data:
            break
        response = 'False'
        if data['username'] not in userNames:
            userNames[data['username']] = data['password']
            print(userNames)
            response = 'True'
        connection.sendall(str.encode(response))

    connection.close()


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
