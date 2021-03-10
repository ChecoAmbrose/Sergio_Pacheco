from EstudiantesMongo import Estudiantes
from EstudiantesMongo import agregar
from EstudiantesMongo import actualizar
from EstudiantesMongo import eliminar
import re
import sys

# [PV] En clase se vio la libreria PySide, no es posible realizar la revision
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit

class Tarea5(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("Tarea5.ui", self)
        self.botonAgregar.setEnabled(False)
        self.botonEliminar.setEnabled(False)
        self.botonActualizar.setEnabled(False)
        self.botonAgregar.clicked.connect(self.agregarui)
        self.botonVer.clicked.connect(self.leerui)
        self.botonEliminar.clicked.connect(self.borrarui)
        self.botonActualizar.clicked.connect(self.actualizarui)
        self.botonMostrar.clicked.connect(self.MostrarOcultar)
        self.botonAyuda.clicked.connect(self.aiuda)

        self.contrasena.setEchoMode(QLineEdit.Password)
        self.nombre.textEdited.connect(self.textoEditado)
        self.correo.textEdited.connect(self.textoEditado)
        self.contrasena.textEdited.connect(self.textoEditado)
        self.materias.textEdited.connect(self.textoEditado)

    def agregarui(self):
        patroncorreo = "\S+[@]\S+[.]+[a-z]{2,3}$"
        self.statusBar().showMessage('Agregando a la base de datos...')
        name = self.nombre.text()
        mail = self.correo.text()
        passw = self.contrasena.text()
        mat = self.materias.text()
        match = re.match(patroncorreo, mail)
        if match:
            actual = Estudiantes(nombre=name, correo=mail, contrasena=passw, materias=mat)
            agregar(actual)
            self.salida.append(f'Se agregó a {name} a la base de datos.')
            self.statusBar().showMessage('Estudiante agregado!')
        else:
            #self.salida.append('Correo invalido, no se pudo agregar usuario')
            self.salida.insertHtml('<p style="color: red"><br>Correo invalido, no se pudo agregar usuario </p>')
            self.salida.insertHtml('<p style="color: black"><br></p>')
        pass

    def leerui(self):
        self.salida.setText('')
        for estudiantes in Estudiantes.objects:
            #print(f'Nombre: {estudiantes.nombre}\tCorreo: {estudiantes.correo}\tContraseña: {estudiantes.contrasena}\tMaterias: {estudiantes.materias}')
            mensaje = f'Nombre: {estudiantes.nombre} Correo: {estudiantes.correo} Contraseña: {estudiantes.contrasena} Materias: {estudiantes.materias}'
            #print(mensaje)
            self.salida.append(mensaje)
        self.statusBar().showMessage('Base de datos en vista')
        pass

    def borrarui(self):
        funar = self.nombre.text()
        eliminar(funar)
        self.salida.append(f'{funar} eliminad@ de la base de datos')
        pass

    def actualizarui(self):
        en = self.nombre.text()
        reemplazar = self.materias.text()
        actualizar(en, reemplazar)
        self.salida.append(f'Se actualizó la materia en curso de {en}')
        pass

    def textoEditado(self):
        self.statusBar().showMessage('Escribiendo...')

        #Agregar
        if len(self.nombre.text()) >= 3 \
            and len(self.correo.text()) >= 5 \
                and len(self.contrasena.text()) >= 8 \
                    and len(self.materias.text()) >= 5 :
            self.botonAgregar.setEnabled(True)
        else:
            self.botonAgregar.setEnabled(False)

        #Borrar
        if len(self.nombre.text()) >= 3 \
            and len(self.correo.text()) == 0 \
                and len(self.contrasena.text()) == 0 \
                    and len(self.materias.text()) == 0 :
            self.botonEliminar.setEnabled(True)
        else:
            self.botonEliminar.setEnabled(False)

        #Actualizar
        if len(self.nombre.text()) >= 3 \
            and len(self.correo.text()) == 0 \
                and len(self.contrasena.text()) == 0 \
                    and len(self.materias.text()) >= 5:
            self.botonActualizar.setEnabled(True)
        else:
            self.botonActualizar.setEnabled(False)

    #Mostrar Ocultar Contraseña
    def MostrarOcultar(self):

        if self.contrasena.echoMode() == QLineEdit.Password:
            self.contrasena.setEchoMode(QLineEdit.Normal)
            self.botonMostrar.setText('Ocultar')
        else:
            self.contrasena.setEchoMode(QLineEdit.Password)
            self.botonMostrar.setText('Mostrar')

    def aiuda(self):
        self.salida.setText('')
        self.salida.insertHtml('<p style="color: blue">Para agregar a un alumno a la base de datos, debes llenar todos los campos, el nombre debe ser mayor a 3 caracteres, el correo electrónico debe ser válido, la contraseña debe ser mayor a 8 caracteres.<br><br>Para actualizar la materia de un alumno debes escribir su nombre y la materia nueva que esté cursando. El campo de correo y de contraseña deben estar vacios.<br><br>Para eliminar a un alumno de la base de datos debes escribir su nombre, los demás campos deben estar vacíos.</p>')
        self.salida.insertHtml('<p style="color: black"><br></p>')


if __name__ == "__main__":
    app = QApplication([])
    widget = Tarea5()
    widget.show()
    sys.exit(app.exec_())

