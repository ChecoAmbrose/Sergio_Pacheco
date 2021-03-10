import socket
import pickle
from estudiante import Estudiante

class cliente:

    def __init__(self):
        self.host = '3.16.226.150'
        self.conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self, puerto):
        self.conexion.connect((self.host, puerto))
        #print("Conexión exitosa")
        respuesta = f'Conectado al servidor 3.16.226.150 en el puerto {puerto}'
        return respuesta

    def desconectar(self):
        self.conexion.close()

    def enviar(self,paquete):
        serializado = pickle.dumps(paquete)

        if isinstance(paquete, Estudiante):
            self.conexion.send(serializado)
            res = self.conexion.recv(1024)
            return res.decode()
        else:
            self.conexion.send(b'INI')
            res = self.conexion.recv(1024)
            final = res

            if len(serializado) < 1024:
                self.conexion.send(serializado)
                res = self.conexion.recv(1024)
                final = final + res

            else:
                continuar = True
                inicio = 0

                while continuar:
                    chunk = serializado[ inicio : inicio + 1024]

                    if not chunk:
                        continuar = False
                        continue

                    self.conexion.send(chunk)
                    res = self.conexion.recv(1024)
                    final = final + res

                    inicio += 1024

            self.conexion.send(b'FIN')
            res = self.conexion.recv(1024)
            final = final + res
            return final.decode()