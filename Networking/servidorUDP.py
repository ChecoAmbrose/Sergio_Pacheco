import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
puerto = 12345

sock.bind((host,puerto))

while True:
    print('Esperando Respuesta')

    info, direccion = sock.recvfrom(1024)

    print(f"Mensaje: {info.decode()} desde {direccion}")