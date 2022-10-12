#Por el momento las preguntas saldran en la consola, luego las mostraremos en la ventana del juego
import os #importamos os para la funcion "borrar_consola"
import random #importamos random para que las respuestas salgan de manera aleatoria
from preguntas import preguntas

n_pregunta = 0

base_de_preguntas = []
renglones = preguntas.split("\n") #dividimos toda la cadena de texto de "preguntas" en una lista, despues del "\n" se tomara como un nuevo elemento en la lista
cantidad_de_preguntas = len(renglones) #con cada renglon sabremos la cantidad de preguntas que tendremos

pregunta_escogida = []
opciones = []
pregunta = ""
respuesta = ""

for i in range(cantidad_de_preguntas):  #recorremos con un for la cantidad de preguntas
    if (renglones[i] == ""):
        continue #si cada renglon tiene una cadena de caracter bacia le colocamos que continue, asi evitamos que renglones vacios nos generen preguntas vacias
    preguntas.append(renglones[i].split("\t")) #a la lista "preguntas" le agregamos cada elemento de los "renglones". preguntas con sus respectivas respuestas

def borrar_consola (): #como por el momento el programa se ejecuta por medio de la consola, creamos la funcion para que no quede registro de lo anterior que hicimos con preguntas
    os.system("cls" if os.name == "nt" else "clear")

def escoger_pregunta (n):
    global pregunta, respuesta, opciones #colocamos las variables "pregunta", "respuesta" y "opciones" como variables globales para que se puede acceder a ellas desde cualquier parte del programa.

    pregunta_escogida = base_de_preguntas[n]
    pregunta = pregunta_escogida[0] #las preguntas estan en el subindice 0 de la "base_de_preguntas"
    respuesta = pregunta_escogida[1] #las respuestas estan en el subindice 1 de la "base_de_preguntas"
    opciones = pregunta_escogida[1:] #las diferentes opciones se toman desde el subindice 1 hasta el ultimo
    for i in range (4): #usamos un for para que no se genere un patron en donde coloca la respuesta correcta en el subindice 0 o en el 1
        random.shuffle(opciones) #con esto las opciones salen en aleatorio
    return pregunta_escogida

def mostrar_pregunta():  #con esta funcion mostramos la pregunta junto con sus posibles respuestas
    borrar_consola()
    print()
    print(pregunta)
    print("A.", opciones[0])
    print("B.", opciones[1])
    print("C.", opciones[2])
    print("D.", opciones[3])
    print()

def opcion_respuesta ():
    respuesta_usuario = ""
    opciones_validas = ["a", "b", "c", "d", "A", "B", "C", "D"]
    while True:
        respuesta_usuario = input("ingrese su respuesta: ").lower() #aqui le pedimos al usuario que ingrese una respuesta
        if not (respuesta_usuario in opciones_validas):
            print("Respuesta no valida, vuelva a colocar su respuesta") #si el ususario coloca una opcion diferente a las que pusimos en "opciones_validas" se imprime el mensaje
            #esto se coloca con el fin de mirar si las preguntas salen con las opciones de manera aleatoria, luego se borrara esto
            continue
        break #para que este ciclo no se repita de manera infinita colocamos un break
    return opciones_validas.index(respuesta_usuario)

def jugar(): #tomamos las funciones hechas anterior mente y las colocamos aqui
    escoger_pregunta(n_pregunta) #tomamos la pregunta #0 en este caso
    mostrar_pregunta()
    if (opciones[opcion_respuesta()] == respuesta): #si la respuesta del usuario es correcta imprime esto
        print("su respuesta es correcta")
        input("presione ENTER para continuar")
    else: #si la respuesta del usuario es diferente imprime esto
        print("su respuesta es incorrecta. \n La respuesta correcta es: "+ respuesta)
        input("presione ENTER para continuar")

while True: #mientras sea verdadero se ejecuta el juego
    try:
        jugar()
    except:
        pass
    n_pregunta += 1  # con esto pasamos a la siguiente pregunta
    if (n_pregunta == cantidad_de_preguntas): #cuando se hallan hecho todas la preguntas el juego se habra terminado
        borrar_consola()
        print("El juego ha terminado")
        break