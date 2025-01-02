import socket
import threading

def client_handler(server_socket, client_address):
  print("Connected to: ", client_address)
  conntected = True
  while conntected:
    upcoming_message_length = server_socket.recv(data).decode(format)
    print("Upcoming message length is", upcoming_message_length)
    if upcoming_message_length:
      message = server_socket.recv(int(upcoming_message_length)).decode(format)
      if message == "disconnected":
        print("Disconnecting with", client_address)
        conntected = False
        server_socket.send("Message Received".encode(format))
        break
      count = 0
      for i in message:
        if i == 'a':
          count += 1
        elif i == 'e':
          count += 1
        elif i == 'i':
          count += 1
        elif i == 'o':
          count += 1
        elif i == 'u':
          count += 1
      server_socket.send("Message Received".encode(format))
      if count == 0:
        server_socket.send("Not enough vowels.".encode(format))
      elif count > 0 and count <= 2:
        server_socket.send("Enough vowels I guess".encode(format))
      elif count > 2:
        server_socket.send("Too many vowels".encode(format))
  server_socket.close()
format = "utf-8"

data = 16
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
  
  