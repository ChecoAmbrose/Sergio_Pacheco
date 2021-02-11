
# Listas
lista = ['hola', 2, 3.4, False, [1,'test'], 2, 'hola']
lista2 = list()

print(f'Lista: {lista}')
print(f'Lista2: {lista2}')

print(type(lista))


#Tuplas

tupla = ('hola', 2, 3.4, False, [1,'test'], 2, 'hola', 2) #Se puede crear sin los parentesis
#tupla = 'hola', 2, 3.4, False, [1,'test'], 2, 'hola', 2
tupla2 = tuple()

print(f'Tupla creada: {tupla}')

#doble asignación de tuplas (2 pues)
elemento_1, elemento_2 = ('hola', 2, 3.4, True, [1,2, 152], 2, 'hola', 2), ('constante')
print(f'Tupla de elementos: {elemento_1}')
print(f'Tupla de un elemento: {elemento_2}')

#Las tuplas de un elemento (o de varios incluso), pueden sustituir a las ctes
#Las ctes no existen en python como tal


# Agregar elementos a las listas
lista.append('Pedro')
print(f'Lista: {lista}')

# Insertar (agregar (lugar, elemento nuevo)
lista.insert(3,True)
print(f'Lista: {lista}')

#Borrar remove(elemento a eliminar)
lista.remove('hola')
print(f'Lista: {lista}')

#Tomar valor
Es = lista.pop(3)
print(f'Es: {Es}')