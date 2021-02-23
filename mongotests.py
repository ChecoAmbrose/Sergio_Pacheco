from pymongo import  MongoClient

cliente = MongoClient()

print(f'cliente: {cliente}')

db = cliente.mongotests

print(f'db: {db}')

estudiantes = db.estudiantes

estudiante = {}
estudiante['nombre'] = 'Pedro'
estudiante['correo'] = 'algo@hotmail.com'

result = estudiantes.insert_one(estudiante)
print(f'Insert ID: {result.inserted_id}')