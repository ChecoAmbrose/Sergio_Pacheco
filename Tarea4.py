from EstudiantesMongo import Estudiantes
from EstudiantesMongo import agregar
from EstudiantesMongo import leer
from EstudiantesMongo import actualizar
from EstudiantesMongo import eliminar

#Se crean los estudiantes con sus 5 objetos
estudiante1 = Estudiantes(nombre= "Sergio", correo= "algo@hotmail.com", contrasena= "NoNinguna", materias= "Python y C/C++" )
estudiante2 = Estudiantes(nombre= 'Emmanuel', correo=  'nose@algo.com', contrasena=  'contraseña2', materias= "Mecnánica")
estudiante3 = Estudiantes(nombre= 'John', correo=  'nose@spartan.com', contrasena=  'contraseña5', materias= "Academia")

#Se agregan los estudiantes a la base de datos students.db
agregar(estudiante1)
agregar(estudiante2)
agregar(estudiante3)

#Se leen los estudiantes de la base de datos
print("Base de datos creada")
leer()

#Alguno requerirá actualizar sus materias en curso
#la información de los estudiantes

#Ejercicio de prueba
#Sergio actualizará su materia a Circuitos
#en = "Sergio"
#reemplazar = "Circuitos"
#actualizar(en , reemplazar)

actualizar("Sergio", "Circuitos")
actualizar("Emmanuel", "Aeronautica")
actualizar("John", "Armamentistica")
print("\nDespués de actualizar las materias")
leer()

#Ahora se elimina a un estudiante
funar = "Emmanuel"
eliminar(funar)
#Se vuelve a leer la base de datos para observar los cambios
print("\nDespués de eliminar a un estudiante expulsado")
leer()

