import random #se importa la libreria random para que la compu pueda elegir una opcion de manera aleatoria

#Definiendo la función que ejecuta el juego de piedra papel o tijeras
def jugar():
    seleccion = ['Piedra','Papel','Tijeras']
    aleatorio=random.randint(0,2) #Genera un número aleatorio entre 0 y 2, puesto que son los
    #espacios de la lista seleccion


    PC=seleccion[aleatorio] #PC toma el valor de la lista con su número aleatorio

    #while para validar que la opción se encuentre entre 1 y 3
    val=0
    while val == 0:
        x=int(input("Elije Piedra (1), Papel (2), o Tijeras (3)\n"))
        if x < 4 and x > 0 :
            val = 1
        else:
            print('ELIJE UNA OPCIÓN VALIDA CTM\n')

    #Hay 3 opciones, pero el conteo de lugares de selección empieza en 0, por lo que al valor ingresado
    #se le resta 1 para poder tomar un valor de la lista selección correctamente
    x=x-1
    YO=seleccion[x]

    #Mensajes se victoria o derrota
    win="Ganaste!!"
    lose="Perdiste :("

    #Pa que veas que la compu no hace trampa al decidir ganador
    print(f'Tú elegiste {YO}')
    print(f'Tu compu eligió {PC}\n')

    #Comparando respuesta de pc y del usuario
    if PC == YO:
        print("Empate!")

    if YO == 'Piedra':
        if PC == 'Papel':
            print(lose)
        if PC == 'Tijeras':
            print(win)

    if YO == 'Papel':
        if PC == 'Piedra':
            print(win)
        if PC == 'Tijeras':
            print(lose)

    if YO == 'Tijeras':
        if PC == 'Papel':
            print(win)
        if PC == 'Piedra':
            print(lose)

