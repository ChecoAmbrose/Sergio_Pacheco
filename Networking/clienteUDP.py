import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
puerto = 12345

mensaje = 'Holaaaa'.encode()

sock.sendto(mensaje,(host,puerto))