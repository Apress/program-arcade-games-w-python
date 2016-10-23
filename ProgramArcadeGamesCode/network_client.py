# Connect to port 12345
import socket

port = 12345
host = socket.gethostname()
# host = '10.1.21.1'

message_string = "I've connected!"
message_data = message_string.encode("utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(message_data)
s.close()
print("Received")
