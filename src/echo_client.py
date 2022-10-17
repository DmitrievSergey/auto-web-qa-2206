import socket

host = '127.0.0.1'
port = 1233

client_socket = socket.socket()
print('Waiting for connection')
try:
    client_socket.connect((host, port))
except socket.error as e:
    print(str(e))

resp = client_socket.recv(1024)
print(resp.decode('utf-8'))
while True:
    msg = input('Your message: ')
    client_socket.send(str.encode(msg))
    resp = client_socket.recv(1024)
    print(resp.decode('utf-8'))
    if msg == 'BYE':
        break

client_socket.close()
