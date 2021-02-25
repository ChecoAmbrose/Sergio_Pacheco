import socket
import pickle
from estudiante import Estudiante


def main():

    s = socket.socket()

    host = '3.16.226.150'
    puerto = 9999

    s.connect((host, puerto))

    estudiante = Estudiante('Sergio Pacheco Franco', 'elite_shergio@hotmail.es', 'No')
    estudiante_seriado = pickle.dumps(estudiante)

    s.send(estudiante_seriado)

    res = s.recv(1024)
    print(f'Respuesta: {res.decode()}')
    s.close()


if __name__ == '__main__':
    main()