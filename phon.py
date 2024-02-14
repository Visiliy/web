import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2001))
server.listen(4)
print('Worgind......')

client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
content = 'Hello my dear brother Kostya'.encode('utf-8')
client_socket.send(HDRS.encode('utf-8') + content

Key = 'http://127.0.0.1:2001/recuest'
