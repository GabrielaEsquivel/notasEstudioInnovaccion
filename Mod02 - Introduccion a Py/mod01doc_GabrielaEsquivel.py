# program.py

# Para programar hay que especificar instrucciones que nos ayuden a
# encontrar el resultado deseado.
# Una instrucción podría imprimir algún texto o
# calcular algo, por ejemplo, el siguiente bloque de código:


sum = 1 + 2
print(sum)

# Sum es el resultado de una suma de 1 y 2.
# Print() es una función impresión, en donde, pasándole un parámetro (param)
# en este caso "sum", imprime el resultaod de la suma realizada.

print('¡Hola! desde la consola')
# Ejemplo de impresión en pantalla de  print('Hola desde la consola')
# Este resultado se podrá ver en una consola.
# Una consola es una aplicación de línea de comandos que te permite 
# interactuar con el sistema operativo. En la consola, puedes ejecutar 
# comandos y programas. También puedes ingresar información y mostrar 
# información como texto en la pantalla.

# Variables
# Las variables nos ayudan a recordar7guardar valores a lo largo de
# la ejecución de un programa.
# Por ejemplo:
sum = 1 + 2 # resultado : 3 variable: sum
product = sum * 2 # resultado: 6 variable: product
print(product) # Imprime 6

# Tipos de datos
# Una variable asume un tipo de datos.
# Algunos de los tipos se pueden dividir en las siguientes "categorías"
# Númericos (con o sin decimales):
# int, float, complex. Ej num = 2
# Texto (cadena de carateres):
# str, Ej str = "una oración"
# Booleano (booleano, true/false)
# booleano, Ej 

planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri) # la función type(param) nos ayudará a descubrirlo
#Imprimirá float


# Operadores
# Los operadores le permiten realizar cálculos sobre variables y sus valores
#  <left side> <operator> <right side>
left_side = 10
right_side = 5
left_side / right_side 
# Operador: / Resultado: 2 (división)

# En el caso de Python, contamos con los operadores:
# aritméticos y de asignación.
# --- aritméticos ---
# suma (+) resta (-) multiplicación (*) división (/)
# --- asignación ---
# asignación (=) suma y asignación (+=)
# resta y asignación (-=) división y asignación (/=)
# multiplicación y asignación (*=)

#Fechas
# Una fecha en un programa generalmente significa
# tanto la fecha del calendario como la hora.

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

print("Today's date is: " + str(date.today()))
# Hay que convertir la fecha en string para que se pueda
# imprimir de manera correcta en la consola.


# Entrada de usuario 
# para obtener data del usuario, es decir, que el lo teclee, por ej.
# habrá que usar la función input()

print("¡Bienvenido!")
name = input("Introduzca su nombre: ")
print("Saludos, " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))
# Hay que convertir la data recibida (que está en string)
# a un tipo número para que haga el cálculo correcto. de otra
# manera lo único que el print hará será concatenar (unir)
# los números ingresados. 

