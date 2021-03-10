from estudiante import Estudiante
import sys
import re
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
        self.consola.append(res)
        self.puerto.setEnabled(False)

        if puerto == 9999 :
            self.botonLista.setEnabled(True)
        elif puerto == 9997 :
            self.botonLista.setEnabled(True)
            self.botonEnviar.setEnabled(True)
        else:
            self.puerto.setEnabled(True)
            mensaje = f'La conexión por el puerto {puerto} no es útil para este programa'
            self.consola.append(mensaje)
            self.cliente.desconectar()


    def lista(self):
        patroncorreo = "\S+[@]\S+[.]+[a-z]{2,3}$"
        nombre = self.nombre.text()
        correo = self.correo.text()
        password = self.password.text()
        match = re.match(patroncorreo, correo)
        if match:
            estudiante = Estudiante(nombre, correo, password)
            res = self.cliente.enviar(estudiante)
            self.consola.append(res)
            self.botonLista.setEnabled(False)
            self.puerto.setEnabled(True)
        else:
            #self.salida.append('Correo invalido, no se pudo agregar usuario')
            self.consola.insertHtml('<p style="color: red"><br>Correo invalido, no se pudo agregar usuario </p>')
            self.consola.insertHtml('<p style="color: black"><br></p>')


    def abrirarchivo(self):
        archivo = QFileDialog.getOpenFileName(filter='*.zip')
        self.archivo.setText(archivo[0])

    def archivozip(self):
        archivo = self.archivo.text()
        if archivo == 'Ruta del archivo...':
            mensaje = "No has seleccionado nada!!"
            self.consola.setText(mensaje)
        else:
            zip = open(archivo, 'rb')
            res = self.cliente.enviar(zip.read())
            self.consola.append(res)
            self.puerto.setEnabled(True)
            self.botonEnviar.setEnabled(False)

if __name__ == '__main__':
    app = QApplication([])
    widget = proyecto()
    widget.show()
    sys.exit(app.exec_())