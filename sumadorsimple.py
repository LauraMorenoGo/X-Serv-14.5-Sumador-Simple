#!/usr/bin/python3
"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #Al socket le añadimos opciones adicionales 
                                                                #REUSEADDR: el puerto no se libera directamente
mySocket.bind(('localhost', 1234))  #socket.gethostname(): coge el nombre de tu máquina

mySocket.listen(5)

vacio = 0   #Definimos operando1 porque sino da error al no estar declarado

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        url = recvSocket.recv(2048)
        print('Answering back...')
        
        try:
            troceo = url.split()[1][1:] #Cuando se imprime en el terminal nos quedamos con el segundo elemento (/numero) 
                                        #y de ahi con el numero sólo
            operando = int(troceo)
            
            if vacio == 0:  #Significa que es el primer operando que metemos, no ha habido otro antes  
            
                operando1 = operando   #Lo asignamos como primer operando
                
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1>Por favor, introduzca el segundo operando de la suma</h1></body></html>" + "\r\n", 'utf-8'))  
            
                vacio = 1   #Con esto decimos que ya tenemos el primer operando, por lo tanto, para el segundo se va 
                            #a meter por la rama del else
            
            else:
        
                operando2 = operando    #En este caso el operando es el segundo que introducimos
                sumar = operando1 + operando2    #Sumamos el primer operando introducido y el segundo
            
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1>La suma de " + str(operando1) + " y " + str(operando2) + " es igual a " + str(sumar) + "</h1></body></html>" + "\r\n", 'utf-8'))
            
                vacio = 0   #Para volver a empezar
               
        
        except ValueError:
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1>Introduzca un numero despues de /</h1></body></html>" + "\r\n", 'utf-8'))    #Poniendo la excepción al final no sale el doble mensaje en la web que salía al tenerlo antes del if
                  #ya que si no se introduce ningún número no entra por el if
            
        recvSocket.close()    
        
            
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()    #Cierro el socket
