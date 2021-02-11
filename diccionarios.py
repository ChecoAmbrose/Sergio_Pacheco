diccionario_1 = {}
diccionario_2 = dict()

print(f'diccionario: {diccionario_1}')
print(f'tipo: {type(diccionario_1)}')

diccionario_1[1]='uno'
diccionario_1[4.5]='cuatro punto cinco'
diccionario_1['Uno']='uno'
diccionario_1[False]='E falso'

print(f'diccionario[1]: {diccionario_1[1]}')
print(f'diccionario[4.5]: {diccionario_1[4.5]}')
print(f'diccionario["Uno"]: {diccionario_1["Uno"]}')
print(f'diccionario[False]: {diccionario_1[False]}')

diccionario_2 = {5: 'cinco', 7.0: 'siete punto cero'}
print(diccionario_1)
print(diccionario_2)