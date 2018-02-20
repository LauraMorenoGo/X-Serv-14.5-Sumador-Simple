#!/usr/bin/python3
"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

#EJERCICIO HECHO EN CLASE

import socket
import calculadorav2

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #Al socket le añadimos opciones adicionales 
                                                                #REUSEADDR: el puerto no se libera directamente
mySocket.bind(('localhost', 1234))  #socket.gethostname(): coge el nombre de tu máquina

mySocket.listen(5)


try:
    while True:

        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        
        print('Request received:')
        bytes_received = recvSocket.recv(2048)
        request = str(bytes_received, 'utf-8')
        
        #Proceso petición y veo que me piden (nuestro yo ahora!)
        
        print(request)
        resource = request.split()[1]
        print("Resource:", resource)
        _, op1, operacion, op2 = resource.split('/')
        print(op1, operacion, op2)
        
        #Hago lo que me piden
        
        num1 = int(op1)
        num2 = int(op2)
                       
        resultado = calculadorav2.funciones[operacion](num1, num2)
        
        #Respondo (en consecuencia)
        
        print('Answering back...')        
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + str(resultado), 'utf-8'))    
        
        recvSocket.close()    
        
            
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()    #Cierro el socket
