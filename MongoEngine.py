from mongoengine import *
from datetime import datetime

connect('mongoengine', host='localhost', port=27017)

class Post(Document):
    Nombre = StringField(required=True, max_length=20)
    Correo = StringField(required=True)
    Contrasena = StringField(required=True, max_length=20)
    Materias = StringField(required=True, max_length=200)


#Método para creación.
if __name__ == '__main__':
    post = Post(Nombre='Sergio', Correo='elite@hotmail.com', Contrasena='No', Materias='Python,C/C++')

    post.save()        #Comentado para no crear multiples bases de datos iguales
    print(f'Nombre: {post.Nombre} \nCorreo: {post.Correo} \nContrasena: {post.Contrasena} \nMaterias: {post.Materias}')
