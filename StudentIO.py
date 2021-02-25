import sqlite3


class estudiantes:
    nombre = ''
    apellido = ''
    correo = ''
    contrasena = ''
    NUA = 0

    def __init__(self, nombre, apellido, correo, contrasena, NUA):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.NUA = NUA


# Se necesita una manera de conexión, con un objeto
conexion = sqlite3.connect('students.db')

# Para poder usar usar los comandos de SQLite facilmente
c = conexion.cursor()

# Creando espacio para los datos (5 objetos)
c.execute("""CREATE TABLE IF NOT EXISTS estudiantes (
            nombre text,
            apellido text,
            correo text,
            contrasena text,
            NUA integer)""")


# Funciones
# Guardar estudiantes
def agregar(estu):
    with conexion:
        c.execute("INSERT INTO estudiantes VALUES (:nombre, :apellido, :correo, :contrasena, :NUA)",
                   {'nombre': estu.nombre, 'apellido': estu.apellido, 'correo': estu.correo, 'contrasena': estu.contrasena, 'NUA': estu.NUA})


#buscar en la base de datos
def buscar(nombre):
    c.execute("SELECT * FROM estudiantes WHERE nombre=:nombre", {'nombre': nombre})
    return c.fetchall()


#Leer base de datos
def leer():
    c.execute("SELECT * FROM estudiantes ")
    db = c.fetchall()
    print(db)


# Actualizar datos (contraseña)
def actualizar(estu, contrasena):
    with conexion:
        c.execute("""UPDATE estudiantes SET contrasena = :contrasena
        WHERE nombre = :nombre AND apellido = :apellido""",
                  {'nombre': estu.nombre, 'apellido': estu.apellido, 'contrasena': contrasena})


# Eliminar algún estudiante
def borrar(estu):
    with conexion:
        c.execute("DELETE from estudiantes WHERE nombre = :nombre AND apellido = :apellido",
                  {'nombre': estu.nombre, 'apellido': estu.apellido})