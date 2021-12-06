import socket
import json

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)


def registration():
    userName = input('enter username\n')
    password = input('enter password\n')
    unp = {'username': userName, 'password': password}
    ClientMultiSocket.send(json.dumps(unp).encode('utf-8'))

    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    if res == 'False':
        print('Username Taken\n')
        registration()
    print('User Registered\n')

def login():
    pass


while True:
    Input = input('Press:\n 1 for Registration \n 2 for login\n')
    if Input == '1':
        registration()
    if Input == '2':
        login()
    print(res.decode('utf-8'))

ClientMultiSocket.close()
