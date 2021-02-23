import socket

#socket del servidor
sock = socket.socket()
host = socket.gethostname()
port = 9999

#print(sock.fileno())
#print(sock.family)
#print(sock.type)
#print(sock.proto)

sock.bind((host, port))

print("Esperando conexión")
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print(f'Conexión a: {addr}')
    mensaje = 'Hola ' + addr[0]
    conn.send(mensaje.encode())
    conn.close()


#import pickle
#mensaje = 'Hola mundo'
#print(mensaje)
#print(type(mensaje))
#se = mensaje.encode()
#print(se)
#print(type(se))
#sp = pickle.dumps(mensaje)
#print(sp)
#print(type(sp))
#ss = se.decode()
#print(ss)
#print(type(ss))
#usp = pickle.loads(sp)
#print(usp)
#print(type(usp))