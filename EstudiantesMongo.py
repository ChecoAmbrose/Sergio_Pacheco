from mongoengine import *

nombre_db = "IECA"

connect(nombre_db, host='localhost', port=27017)

class Estudiantes(Document):
    nombre = StringField(required=True, max_length=20)
    correo = StringField(required=True, max_length=50)
    contrasena = StringField(required=True, max_length=20)
    materias = StringField(required=True, max_length=100)


# Funciones
# Guardar estudiantes, la función recibe t o d o el dirrecionario estudiantes
# [PV] El parametro es una instancia (objeto) de la clase Estudiantes
def agregar(Estudiantes):
    Estudiantes.save()  # Comentado para no crear multiples bases de datos iguales
    #print(f'Nombre: {Estudiantes.nombre} \nCorreo: {Estudiantes.correo} \nContrasena: {Estudiantes.contrasena} \nMaterias: {Estudiantes.materias}')

#Leer a todos los estudiantes
def leer():
    for estudiantes in Estudiantes.objects:
        print(f'Nombre: {estudiantes.nombre}\tCorreo: {estudiantes.correo}\tContraseña: {estudiantes.contrasena}\tMaterias: {estudiantes.materias}')


#Actualizar los datos, cambian las materias en curso, la función recibe el nombre del estudiante que cursará nueva materia, y la nueva materia
def actualizar(en, reemplzar):
    estudiante = Estudiantes.objects(nombre= en)
    estudiante.update(materias = reemplzar)


#Expulsado, se borrará a un estudiante de la base de datos. La función recibe el nombre para lograr esto.
def eliminar (funar):
    funado = Estudiantes.objects(nombre = funar)
    funado.delete()