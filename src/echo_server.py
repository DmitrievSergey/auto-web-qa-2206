import re
import socket
import datetime
from _thread import start_new_thread


http_response = (
    f"HTTP/1.0 200 OK\r\n"
    f"Server: echo_server\r\n"
    f"Date: {datetime.datetime.now()}\r\n"
    f"Content-Type: text/html; charset=UTF-8\r\n"
    f"\r\n"
)

request_list = []
headers_list = []
end_of_stream = '\r\n\r\n'


def build_request(req):
    l = req.decode()
    lines = re.split('\r\n', l)
    print(lines)
    request_list.append(lines[0].split(' ')[0])
    if lines[0].split(' ')[1].__contains__('=404'):
        request_list.append('404 Not Found')
    else:
        request_list.append('200 OK')
    for i in range(2, len(lines) - 1, 1):
        if len(lines[i]) > 0:
            headers_list.append(lines[i])


def header_out():
    str1 = b''
    for header in headers_list:
        str1 += f"{header}".encode() + f"\n".encode()

    return str1


def handle_client(connection):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print("Received:", data)
            if not data:
                break
            client_data += data.decode()
            if end_of_stream in client_data:
                break
        # Send current server time to the client
        build_request(data)
        connection.send(http_response.encode()
                        + f"Request Method: {request_list[0]}".encode()
                        + f"\n".encode()
                        + f"Request Source: {clientAddress}".encode()
                        + f"\n".encode()
                        + f"Response Status: {request_list[1]}".encode()
                        + f"\n".encode()
                        + header_out()
                        + f"\r\n".encode())
        request_list.clear()
        headers_list.clear()


with socket.socket() as serverSocket:
    # Bind the tcp socket to an IP and port
    serverSocket.bind(("127.0.0.1", 1233))
    # Keep listening
    serverSocket.listen()

    while True:
        (clientConnection, clientAddress) = serverSocket.accept()
        start_new_thread(handle_client, (clientConnection,))
        # handle_client(clientConnection)
        print(f"Sent data to {clientAddress}")
