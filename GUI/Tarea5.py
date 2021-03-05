from EstudiantesMongo import Estudiantes
from EstudiantesMongo import agregar
from EstudiantesMongo import actualizar
from EstudiantesMongo import eliminar
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

class Tarea5(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("Tarea5.ui", self)
        self.botonAgregar.clicked.connect(self.agregarui)
        self.botonVer.clicked.connect(self.leerui)
        self.botonEliminar.clicked.connect(self.borrarui)
        self.botonActualizar.clicked.connect(self.actualizarui)

        self.nombre.textEdited.connect(self.textoEditado)
        self.correo.textEdited.connect(self.textoEditado)
        self.contrasena.textEdited.connect(self.textoEditado)
        self.materias.textEdited.connect(self.textoEditado)

    def agregarui(self):
        self.statusBar().showMessage('Agregando a la base de datos...')
        name = self.nombre.text()
        mail = self.correo.text()
        passw = self.contrasena.text()
        mat = self.materias.text()
        actual = Estudiantes(nombre = name, correo= mail, contrasena= passw, materias= mat )
        agregar(actual)
        self.statusBar().showMessage('Estudiante agregado!')
        pass

    def leerui(self):
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
        pass

    def actualizarui(self):
        en = self.nombre.text()
        reemplazar = self.materias.text()
        actualizar(en, reemplazar)
        pass

    def textoEditado(self):
        self.statusBar().showMessage('Escribiendo...')

        if len(self.nombre.text()) >= 3 \
            and len(self.correo.text()) >= 5 \
                and len(self.contrasena.text()) >= 8 \
                    and len(self.materias.text()) >= 5 :
            self.botonAgregar.setEnabled(True)
        else:
            self.botonAgregar.setEnabled(False)

        if len(self.nombre.text()) >= 3 \
            and len(self.correo.text()) == 0 \
                and len(self.contrasena.text()) == 0 \
                    and len(self.materias.text()) == 0 :
            self.botonEliminar.setEnabled(True)
        else:
            self.botonEliminar.setEnabled(False)

        if len(self.nombre.text()) >= 3 \
            and len(self.correo.text()) == 0 \
                and len(self.contrasena.text()) == 0 \
                    and len(self.materias.text()) >= 5:
            self.botonActualizar.setEnabled(True)
        else:
            self.botonActualizar.setEnabled(False)


if __name__ == "__main__":
    app = QApplication([])
    widget = Tarea5()
    widget.show()
    sys.exit(app.exec_())


#leer()

#actualizar("Sergio", "Circuitos")
#leer()

#funar = "Emmanuel"
#eliminar(funar)
#eer()

