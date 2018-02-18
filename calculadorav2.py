#!/usr/bin/python3

import sys


def suma(op1, op2):
    return op1 + op2
    
def resta(op1, op2):
    return op1 - op2

def div(op1, op2):
    return op1 / op2
    
def mult(op1, op2):
    return op1 * op2

funciones = {'sumar': suma, 'restar': resta, 'multiplicar': mult, 'dividir': div}   

if __name__ == '__main__':      #Solo realiza esto si se usa la calculadora como tal

    operaciones = ['sumar', 'restar', 'multiplicar', 'dividir']

    if len(sys.argv) != 4:
        print('Número de argumentos erróneo. Introduzca una función y dos operandos')
    else:
        for v in range(len(operaciones)):           #Comprueba que el primer argumento esté en 
                                                    #la lista de las operaciones que se pueden hacer
            if sys.argv[1] != operaciones[v]: 
                if v == 3:
                    print('Argumento 1 incorrecto, introduzca una palabra de la lista:')
                    print(operaciones)  
            else:
                break
     
        try:      
            if sys.argv[1] == 'sumar':                  #Suma
                resultado = float(sys.argv[2]) + float(sys.argv[3])
                print(resultado)
            elif sys.argv[1] == 'restar':               #Resta
                resultado = float(sys.argv[2]) - float(sys.argv[3])
                print(resultado)
            elif sys.argv[1] == 'multiplicar':          #Multiplicación
                resultado = float(sys.argv[2]) * float(sys.argv[3])
                print(resultado)
            elif sys.argv[1] == 'dividir':              #División
                try:
                    resultado = float(sys.argv[2]) / float(sys.argv[3])
                    print(resultado)
                except ZeroDivisionError:               #En la división nos puede saltar 
                                                        #la excepción si el denominador es 0
                    print('Introduzca como segundo operando un número distinto de cero')
        except ValueError:
            print('El argumento 2 y 3 tienen que ser números')  #Salta excepción si los argumentos 
                                                                #2 y 3 no son números




