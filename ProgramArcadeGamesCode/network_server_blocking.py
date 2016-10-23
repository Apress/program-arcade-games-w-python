import socket
import time

host = ''
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print("Listening")

while True:
    conn, addr = s.accept()
    print("Connected by: ", addr)
    data = conn.recv(1024)
    if data:
        data_string = data.decode("utf-8")
        print(data_string)
        conn.close()

print("End Listening")
