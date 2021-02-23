from mongoengine import *
from datetime import datetime

connect('mongoengine', host='localhost', port=27017)

class Post(Document):
    titulo = StringField(required=True, max_length=200)
    contenido = StringField(required=True)
    autor = StringField(required=True, max_length=50)
    fecha = DateField(default=datetime.now())


#Método para creación.
if __name__ == '__main__':
    post = Post(titulo='Ejemplo', contenido='Prueba',autor='Yo')

    #post.save()        Comentado para no crear multiples bases de datos iguales
    print(f'Titulo: {post.titulo} \nContenido: {post.contenido} \nAutor: {post.autor}')
