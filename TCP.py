import socket

s = socket.socket()
host = socket.gethostname()
port = 9999

s.bind((host,port))

print("Esperando conexión")
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Conexión a: ",addr)
    conn.send("El servidor te saluda!".encode())
    conn.close()
