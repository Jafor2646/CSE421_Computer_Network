import socket

def sending_message(msg):
  message = msg.encode(format)
  message_length = len(message)
  message_length_str = str(message_length).encode(format)
  message_length_str += b" "*(data-message_length)

  client.send(message_length_str)
  client.send(message)
  print("Sent from server: ",client.recv(128).decode(format))




format = "utf-8"

data = 16
port = 5050
device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
client_ip = socket.gethostbyname(device_name)
server_socket_address = (server_ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_socket_address)

while True:
  msg = input("Enter Something: ").lower()
  sending_message(msg)

  if msg == "disconnected":
    break