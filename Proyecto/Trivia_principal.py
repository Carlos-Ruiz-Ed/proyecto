import os
"""permite realizar operaciones con el sistema operativo por ejemplo
abrir archivos, en el programa se ocupa para mandar a llamar
los archivos de las preguntas y respuestas e para poder guardar
las preguntas que sean agregadas."""

import sys
"""permite usar instruciones diractamente con el
interpretador en el programa es usado para cerrar el programa."""

import random
"""permite obtener valores aleatorios, en el programa
se ocupa para obtener indices aleatorios para seleccionar la pregunta
y para que las respuestas aparescan de diferente forma."""

import pickle
"""permite serializar variables para almacenarlos mas
facilmente, se ocupa en el programa para serialzar las variables de
la base de datos de preguntas y respuestas para poder guardarlos y
llamarlos de los archivos desde el programa."""

import time
"""permite realizar funciones que requieran tiempo en el programa se
usa para dar ligeras pausas entre algunas impresiones y de igual forma
para delimitar el tiempo permitido para contestar las preguntas"""

#Variables globales        
global num_pregunta
global puntaje
num_pregunta=1
puntaje=0
global pregunta

#==================       =================#

class Preguntas():
    def __init__ (self):
        """Clase que define los valores para las preguntas y las respuestas como diccionarios
        vacios para que despues se puedan asignar los valores guardados
        """
        self.categorias = {}
        self.respuestas = {}


pregunta = Preguntas() 

###===========================       =======================###  

'''Funcion recuperada de http://stackoverflow.com/pregunta_enunciadas/17254780/printing-extended-ascii-characters-in-python-3-in-both-windows-and-linux'''
def ClearScreen(headerMessage, headerSize = 10):
    """Esta funcion agrega un marco cuadrado
    alrededor del texto enviado como 
    headerMessage"""
    
    dic = {
    '\\' : b'\xe2\x95\x9a',
    '-'  : b'\xe2\x95\x90',
    '/'  : b'\xe2\x95\x9d',
    '|'  : b'\xe2\x95\x91',
    '+'  : b'\xe2\x95\x94',
    '%'  : b'\xe2\x95\x97',
    }

    def decode(x):
        return (''.join(dic.get(i, i.encode('utf-8')).decode('utf-8')for i in x))

    print(decode("+%s%%" % ('-' * headerSize)))
    print(decode("|%s|"  % (headerMessage.center(headerSize))))
    print(decode("\\%s/" % ('-' * headerSize)))

###===========================       =======================###  

def menu_principal():
    """
    (uso de condicionales, funciones)
    funcion principal donde se despliega un menu para que el usuario escoja que
    hacer dependiendo la entrada la funcion que se despliega
    """
    
    with open('Preguntas','rb') as f: 
        pregunta.categorias=pickle.load(f) #asigna los valores para las preguntas
        f.close()
    with open('Respuestas','rb') as f: 
        pregunta.respuestas=pickle.load(f) #asigna los valores para las respuestas
        f.close()

    ClearScreen("¡Bienvenido a la TRIVIA!", 50)
    print ("1) Empezar juego\n\
2) Agregar Pregunta a la trivia\n\
3) Salir del juego\n\
                                         help")
    opcion = str(input("--> "))
    
    if opcion == "1":
        Juego(num_pregunta,puntaje)
    elif opcion == "2":
        Add_Pregunta()
    elif opcion == "3":
        sys.exit()
    elif opcion == "help":
        print(instrucciones())
        time.sleep(5)
        menu_principal()
    else:
        print("Opcion invalida")
        pausa = str(input("Presiona Enter para continuar\n"))
        menu_principal()

#==================       =================#
def instrucciones():
    """
    La funcion instrucciones imprime las instrucciones en la consola
    para que el usuario pueda leerlas y saber la dinamica del juego.
    """

    return("\nEl juego consiste de 6 preguntas una para cada una de las \n\
siguientes categorias: Geografia, Entretenimiento, Historia, Arte, \n\
Ciencias y Deportes. \n\
Junto con la pregunta se mostraran cuatro opciones de respuesta; \n\
para selecionar la respuesta teclee la respuesta no el inciso.\n\
Para regresar al menu principal durante el juego teclee r, para \n\
acceder a las instrcciones teclee h.\n")
#==================       =================#
        
def Add_Pregunta():
    """
    (uso de condicionales, listas, listas concatenadas, archivos)
    Funcion que permite al usuario agregar preguntas a la base de datos
    se ingresa la categoria las opciones la pregunta y la respuesta
    si la categoria no existe se reinicia la funcion. Posteriormente guarda
    lo ingresado en los archivos como datos en binario para agregarlos a la
    base de datos de preguntas
    """

    Categoria=str(input("\nEscoje una categoria (Geografia, Entretenimiento, \
Historia, Arte, Ciencias,\nDeportes): \n--> "))
    try:
        Pregunta_opciones = pregunta.categorias[Categoria]
    except:
        print("Categoria invalida")
        pausa = str(input("Presiona Enter para continuar\n"))
        Add_Pregunta()
        
    Pregunta=str(input("Pregunta --> "))
    
    A=str(input("A) --> "))
    B=str(input("B) --> "))
    C=str(input("C) --> "))
    D=str(input("D) --> "))
    
    Opciones=[Pregunta,A,B,C,D]
    Pregunta_opciones.append(Opciones)
    pregunta.categorias[Categoria]=Pregunta_opciones
    
    Correcta=str(input("Respuesta correcta --> "))
    print("")
    
    pregunta.respuestas[Pregunta]=Correcta
    
    with open('Preguntas','wb') as f:
        pickle.dump(pregunta.categorias,f)
        f.close()
    with open('Respuestas','wb') as f:
        pickle.dump(pregunta.respuestas,f)
        f.close
    menu_principal()

#==================       =================#   
              
def Juego(num_pregunta,puntaje):
    """
    (ciclos,listas,listas anidadas,funciones,condicionales,operadores)
    recibe: numero de pregunta y actual
    Funcion que permite el jugar el juego. Cambia la categoria cada pregunta
    mientras el numero de pregunta sea menor igual a 6 enviando despues de cada
    pregunta la respuesta correcta, el numero de pregunta y el puntaje al comparador
    de respuestas.
    Las preguntas son escogidas aleatoreamente por categoria con la ayuda de un contador
    y la libreria random. De igual forma las respuestas son impresas en orden aleatorio.
    Una vez contestadas 6 preguntas manda el puntaje a la funcion del fin del juego.
    """
    while num_pregunta <= 6:
        cont = -1
        if num_pregunta == 1:
            categoria = "Geografia"
        elif num_pregunta == 2:
            categoria = "Entretenimiento"
        elif num_pregunta == 3:
            categoria = "Historia"
        elif num_pregunta == 4:
            categoria = "Arte"
        elif num_pregunta == 5:
            categoria = "Ciencias"
        elif num_pregunta == 6:
            categoria = "Deportes"
            
        Preguntas = pregunta.categorias[categoria]
        for i in Preguntas:
            cont += 1
        pregunta_random = random.randint(0,cont)
        Pregunta = Preguntas[pregunta_random]
        
        t=[i for i in range (1,5)]
        A = int(random.randint(1,4))
        t.remove(A)
        B = int(random.choice(t))
        t.remove(B)
        C = int(random.choice(t))
        t.remove(C)
        D = random.choice(t)
        
        pregunta_enunciada = str(Pregunta[0])
        A = str(Pregunta[A])
        B = str(Pregunta[B])
        C = str(Pregunta[C])
        D = str(Pregunta[D])

        print("")
        ClearScreen(pregunta_enunciada, 70)
        print("A) %s\n\
B) %s\n\
C) %s\n\
D) %s\n\
                         %i/6\n\
                         help" % (A,B,C,D,num_pregunta))

        
        respuesta_correcta = pregunta.respuestas[pregunta_enunciada]
        evaluacion(respuesta_correcta,num_pregunta,puntaje)

    fin_del_juego(puntaje)

#==================       =================#

def evaluacion(respuesta_correcta,num_pregunta,puntaje):
    """(operadores, condicionales)
    recibe: La respuesta correcta a la preguta, el numero de pregunta
    y el puntaje acumulado.
    Funcion Auxiliar que evalua la respuesta y la compara con la correcta
    suma al contador de pregunta y suma el puntaje y los regresa a la
    funcion del juego. En caso de que el usuario teclee r se reinicia el
    programa y al teclear h despliega las instrucciones y regresa al
    juego con otra pregunta sin contar la pregunta
    """
    Respuesta= str(input("Respuesta --> ")) 
    if Respuesta == respuesta_correcta:
        print ("Respuesta Correcta\n")
        num_pregunta += 1
        puntaje += 150
    elif Respuesta == "r":
        menu_principal()
    elif Respuesta == "help":
        print(instrucciones())
        time.sleep(5)
        Juego(num_pregunta,puntaje)
    else:
        print ("Respuesta incorrecta\n")
        num_pregunta += 1
    print("Puntaje: %i\n" %(puntaje))
    pausa = str(input("Presiona Enter para continuar\n"))
    Juego(num_pregunta,puntaje)

#==================       =================#

def fin_del_juego(puntaje):
    """(cadena de caracteres,archivos,condicionales)
    
    """
    nombre = str(input("Nombre --> "))
    print ("%s······················%i\n" % (nombre,puntaje))
    puntajes = open ('Puntajes.txt','a')
    puntajes.write("\n" + ("%s······················%i" % (nombre,puntaje)))
    puntajes.close()
    opcion=str(input("Para regresar al menu tecle r, Para terminar el programa \
solo presione enter\n"))
    if opcion == "r":
        menu_principal()
    else:
        sys.exit()
    
#==================       =================#

if __name__ == "__main__":
    menu_principal()
