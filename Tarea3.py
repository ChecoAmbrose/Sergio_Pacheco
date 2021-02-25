from StudentIO import agregar
from StudentIO import leer
from StudentIO import actualizar
from StudentIO import borrar
from StudentIO import conexion
from StudentIO import estudiantes

#Se crean los estudiantes con sus 5 objetos
estudiante1 = estudiantes('Sergio', 'Pacheco', 'elite@algo.com', 'contraseñajsjs', 274251)
estudiante2 = estudiantes('Emmanuel', 'Carrera', 'nose@algo.com', 'contraseña2', 484617)
estudiante3 = estudiantes('Sergio', 'Arturo', 'nose@spartan.com', 'contraseña57', 118471)

#Se agregan los estudiantes a la base de datos students.db
agregar(estudiante1)
agregar(estudiante2)
agregar(estudiante3)

#Se leen los estudiantes de la base de datos
leer()

#Alguno requerirá actualizar su contraseña, otros se pueden dar de baja, por lo que hay 2 funciones para actualizar
#la información de los estudiantes
actualizar(estudiante2, "111111")
borrar(estudiante3)

#Se vuelve a leer la base de datos para observar los cambios
leer()

conexion.close()