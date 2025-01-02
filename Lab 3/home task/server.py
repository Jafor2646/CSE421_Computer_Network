import socket
import threading

def client_handler(server_socket, client_address):
  print("Connected to: ", client_address)
  conntected = True
  while conntected:
    message = server_socket.recv(data).decode(format)
    if message == "-1":
      print("Disconnecting with", client_address)
      conntected = False
      server_socket.send("Message Received".encode(format))
      break
    hours = int(message)
    payment = 0
    if hours >= 0 and hours <= 40:
      payment = hours*200
    elif hours > 40:
      payment = 8000+(300*(hours-40))
    server_socket.send("Message Received".encode(format))
    server_socket.send(f"Your Salary: {payment}".encode(format))
    
  server_socket.close()
format = "utf-8"

data = 3
port = 5050
device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
server_socket_address = (server_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_address)

server.listen()

print("Server is listening...")

while True:
  server_socket, client_address = server.accept()
  thread = threading.Thread(target=client_handler, args=(server_socket, client_address))
  thread.start()
  
  