from JuegoPPoT import jugar

#Mensaje de bienvenida
print("Bienvenido al juego de piedra papel o tijera, jugarás contra tu propio ordenador")

#El juego no acaba hasta que el usuario quiera, para ello el ciclo while
x=0
while x == 0:

    #iniciar juego
    jugar()
    print("\n Quieres jugar de nuevo?? y/n ")
    respuesta=input()
    #terminar el juego
    if respuesta == 'n':
        x=1
        print('Gracias por jugar! vuelva pronto')
