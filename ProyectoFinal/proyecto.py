from estudiante import Estudiante
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit, QFileDialog
from cliente import cliente

class proyecto(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto.ui", self)
        self.cliente = cliente()
        self.servidor.setEnabled(False)
        self.archivo.setEnabled(False)
        self.botonLista.setEnabled(False)
        self.botonEnviar.setEnabled(False)

        self.botonConectar.clicked.connect(self.conectar)
        self.botonLista.clicked.connect(self.lista)
        self.botonBuscar.clicked.connect(self.abrirarchivo)
        self.botonEnviar.clicked.connect(self.archivozip)

    def conectar(self):
        puerto = self.puerto.currentItem().text()
        puerto = int(puerto)
        res = self.cliente.conectar(puerto)
        print(res)
        self.puerto.setEnabled(False)

        if puerto == 9999 :
            self.botonLista.setEnabled(True)
        elif puerto == 9997 :
            self.botonLista.setEnabled(True)
            self.botonEnviar.setEnabled(True)
        else:
            self.puerto.setEnabled(True)
            print(f'La conexión por el puerto {puerto} no es útil para este programa')


    def lista(self):
        nombre = self.nombre.text()
        correo = self.correo.text()
        password = self.password.text()
        estudiante = Estudiante(nombre, correo, password)

        res = self.cliente.enviar(estudiante)
        print(res)

    def abrirarchivo(self):
        archivo = QFileDialog.getOpenFileName(filter='*.zip')
        self.archivo.setText(archivo[0])

    def archivozip(self):
        archivo = self.archivo.text()
        if archivo == 'Ruta del archivo...':
            print("No has seleccionado nada!!")
        else:
            zip = open(archivo, 'rb')
            res = self.cliente.enviar(zip.read())
            print(res)
            self.puerto.setEnabled(True)

if __name__ == '__main__':
    app = QApplication([])
    widget = proyecto()
    widget.show()
    sys.exit(app.exec_())