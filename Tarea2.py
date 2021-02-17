#importar libreria REGEX para poder usar expresiones regulares
import re

#Ingresar información
correo=input("Ingresa un correo electrónico: ")
numero=input("Ingresa un número telefonico (10 digitos): ")
RFC=input("Ingresa un RFC (persona física): ")
CURP=input("Ingresa un CURP: ")


#El patron se divide en el usuario \S+ (cualquier cadena de caracteres de cualquier tamaño), seguido de [@], seguido del proveedor \S+
#Al final necesita un dominio, por lo que se necesita un "." seguido de 2 (o 3) valores alfa numericos, por lo que .mx o .com son validos
patron1="\S+[@]\S+[.]+[a-z]{2,3}$"

#El patron debe admitir "(" y ")" con 2 o 3 numeros intermedios [\(]?[\+]?(\d{2,3})[\)]
#Puede tener o no un espacio [\s]?, y después deben terminar con 7 u 8 números del telefono ((\d{7,8})$)
#Or (|) nos permite dejar más casos sin tener que complicar las condiciones del patron
#En caso que hayan espacios entre los 7 u 8 numeros finales, se repite la condición
#pero permitiendo ahora que el número se pueda dividir en 3 o 4 digitos. Eso si, en caso que se dividan, siempre debe acabar con 4 digitos
patron2="[\(]?[\+]?(\d{2,3})[\)]?[\s]?((\d{7,8})$)|[\(]?[\+]?(\d{2,3})[\)]?[\s]?((\d{3,4}))[\s]?((\d{4})$)|[\(]?[\+]?(\d{2,3})[\)]?[\s]?((\d{3,4}))[-]?((\d{4})$)"

#El RFC requiere 4 letras mayusculas (iniciales nombre), después 6 valores numericos (fecha nacimiento)
#Y por ultimo una homoclave de 3 digitos, como no entiendo del todoo la homoclave, la dejé con valores cualquira (vi ejemplos tanto con números, como con letras) \S{3}$
patron3="^[A-Z]{4}[0-9]{6}\S{3}$"

#Los primeros 10 digitos son lo mismo que en el RFC, a continuación se pone si el individuo es hombre o mujer [HM]?
#Después sigue 2 letras en representación del estado, y 3 que vienen dle nombre, por lo que son 5 letras mayusculas [A-Z]{5}
#Aquí también hay homoclave, pero solo de 2 digitos \S{2}$"
patron4="^[A-Z]{4}[0-9]{6}[HM]?[A-Z]{5}\S{2}$"

#Se crean los 4 resultados
resultado1 = re.match(patron1,correo)
resultado2 = re.match(patron2,numero)
resultado3 = re.match(patron3,RFC)
resultado4 = re.match(patron4,CURP)

#Se evalua si el dato es correcto, y se imprime en pantalla si lo fue o no
#El if de esta manera, dice que el resultado es True siempre que sea diferente de None
#Cuando es None, se imprime que la entrada es invalida
if resultado1:
    print("Correo valido y registrado con éxito")
else:
    print("Correo invalido")

if resultado2:
    print("Telefono valido y registrado con éxito")
else:
    print("Telefono invalido")

if resultado3:
    print("RFC valido y registrado con éxito")
else:
    print("RFC invalido")

if resultado4:
    print("CURP valido y registrado con éxito")
else:
    print("CURP invalido")

#Mostrar coicidencias para pruebas
#print(resultado1)
#print(resultado2)
#print(resultado3)
#print(resultado4)