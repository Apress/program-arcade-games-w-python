import socket
import time

host = ''
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.bind((host, port))
s.listen(1)

print("Listening")

while True:
    try:
        time.sleep(.1)
        conn, addr = s.accept()
        print("Connected by: ", addr)
        data = conn.recv(1024)
        if data:
            data_string = data.decode("utf-8")
            print(data_string)
            conn.close()

    except BlockingIOError:
        """ Do Nothing """

    except KeyboardInterrupt:
        break

print("End Listening")
input("Press any key to exit...")
