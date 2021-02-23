import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999

sock.connect((host,port))
mensaje= sock.recv(1024).decode()

print(mensaje)

sock.close()