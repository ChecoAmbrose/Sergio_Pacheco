import shelve

animals = ["Python", "Algo", "Vision"]

with shelve.open('Prueba') as objecto_shelve:
    objecto_shelve['Animals'] = animals
    objecto_shelve['numero'] = 15
    objecto_shelve['decimal'] = 15.5