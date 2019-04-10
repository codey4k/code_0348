#!/usr/bin/python

import socket
import threading

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        
    def mount(self):
        data_conection = (self.ip, self.port)
        max_connect = 5
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(data_conection)
        server.listen(max_connect)
        print ("Esperando conecciones en %s : %s" % (self.ip, self.port) )
        server, direction = server.accept()
        print("Conexion establecida con %s:%s" % (direction[0], direction[1]))

        while True:
            try:
                data = server.recv(4096)
                print "conectado %s %s" % (direction[0], direction[1])
                print("\x1b[1;32m" + "RECIBIDO: %s" % data)
                instruccion = raw_input("> ")
                server.sendall(instruccion)
                if instruccion == "exit":
                    break
                    if data == "":
                        print "no hay respuesta"
            except:
                pass
           
def main():
    server = Server("0.0.0.0", 3540)
    server.mount()
    
    
if __name__ == "__main__":
    main()
    