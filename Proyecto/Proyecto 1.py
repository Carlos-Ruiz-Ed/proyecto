import os
import sys
import random
import pickle

        
global num_p
global puntaje
num_p=0
puntaje=0
global pregunta

class Preguntas():
    def __init__ (self):
        self.categorias = {}
        self.respuestas = {}


pregunta = Preguntas()

"""Funcion recuperada de http://stackoverflow.com/questions/17254780/printing-extended-ascii-characters-in-python-3-in-both-windows-and-linux. \
esta funcion agrega un marco alrededor del texto selecionado"""
def ClearScreen(headerMessage, headerSize = 10):

    
    dic = {
    '\\' : b'\xe2\x95\x9a',
    '-'  : b'\xe2\x95\x90',
    '/'  : b'\xe2\x95\x9d',
    '|'  : b'\xe2\x95\x91',
    '+'  : b'\xe2\x95\x94',
    '%'  : b'\xe2\x95\x97',
    }

    def decode(x):
        return (''.join(dic.get(i, i.encode('utf-8')).decode('utf-8') for i in x))

    print(decode("+%s%%" % ('-' * headerSize)))
    print(decode("|%s|"  % (headerMessage.center(headerSize))))
    print(decode("\\%s/" % ('-' * headerSize)))

def main():
    with open('Preguntas','rb') as f:
        pregunta.categorias=pickle.load(f)
    with open('Respuestas','rb') as f:
        pregunta.respuestas=pickle.load(f)


    ClearScreen("¡Bienvenido a la TRIVIA!", 50)
    print ("1) Empezar juego\n\
2) Agregar Pregunta a la trivia\n\
3) Multijugador\n\
4) Salir del juego\n")
    opcion = str(input("--> "))
    if opcion == "1":
        Juego(num_p,puntaje)
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        sys.exit()
    else:
        main()

def Add_P():
    global p_r
    p_r={}
    global c_p
    c_p={}
    Categoria=str(input("Categoria:  --> "))
    Pregunta=str(input("Pregunta --> "))
    A=str(input("A)--> "))
    B=str(input("B)--> "))
    C=str(input("C)--> "))
    D=str(input("D)--> "))
    Opciones=[Pregunta,A,B,C,D]
    Correcta=str(input("Respuesta correcta --> "))
    c_p[Categoria]=Opciones
    p_r[Pregunta]=Correcta
    print(p_r,c_p)
    with open('Preguntas','wb') as f:
        pickle.dump(pregunta,f)
    with open('Respuestas','wb') as f:
        pickle.dump(pregunta,f)
    main()
              
def Juego(num_p,puntaje):
    print("Para contestar escribe la respuesta como aparece no el inciso")
    pausa = str(input("Presiona Enter"))
    Pregunta = pregunta.categorias['Hola']
    l=[i for i in range (1,5)]
    A = int(random.randint(1,4))
    l.remove(A)
    B = int(random.choice(l))
    l.remove(B)
    C = int(random.choice(l))
    l.remove(C)
    D = random.choice(l)
    P = str(Pregunta[0])
    A = str(Pregunta[A])
    B = str(Pregunta[B])
    C = str(Pregunta[C])
    D = str(Pregunta[D])
    ClearScreen("Primera pregunta", 50)
    print("%s:\n\
A) %s\n\
B) %s\n\
C) %s\n\
D) %s\n" % (P,A,B,C,D))
    evaluacion(P,num_p,puntaje)


def evaluacion(P,num_p,puntaje):
    Respuesta= str(input("Respuesta --> "))
    if Respuesta == pregunta.respuestas[P]:
        print ("Respuesta Correcta")
        num_p += 1
        puntaje += 100
    else:
        print ("Respuesta incorrecta")
        num_p += 1
    print("Numero de pregunta: %i/10\nPuntaje: %i" %(num_p,puntaje))

    
def MP():
    pass



if __name__ == "__main__":
    main()
