import socket
 
servidor = "127.0.0.1"
puerto = 39421
 
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidor, puerto))
cliente.send("Hola mundo")
respuesta = cliente.recv(1024)
print respuesta