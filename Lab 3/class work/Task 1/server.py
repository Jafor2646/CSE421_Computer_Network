import socket

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
  print("Connected to: ", client_address)
  conntected = True
  while conntected:
    upcoming_message_length = server_socket.recv(data).decode(format)
    print("Upcoming message length is", upcoming_message_length)
    if upcoming_message_length:
      message = server_socket.recv(int(upcoming_message_length)).decode(format)
      print(message)
      if message == "disconnected":
        print("Disconnecting with", client_address)
        conntected = False
      server_socket.send("Message Received".encode(format))
  server_socket.close()