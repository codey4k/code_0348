import socket
import threading

def administrar_clientes(socket_cliente):
    peticion = socket_cliente.recv(1024)
    print "[*] Mensaje recibido: %s" % peticion
    socket_cliente.send("ACK")
    socket_cliente.close()

ip = "0.0.0.0"
puerto = 39421
max_conexiones = 5
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
servidor.bind((ip, puerto))
servidor.listen(max_conexiones)

print "[*] Esperando conexiones en %s:%d" % (ip, puerto)

while True:
    client, direccion = servidor.accept()
    print "[*] Conexion establecida con %s:%d" % direccion[0], direccion[2]
    administrador_de_clientes = threading.Thread(target=administrar_clientes, args=(client))
    administrador_de_clientes.start()