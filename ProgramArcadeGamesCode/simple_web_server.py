import socket       

s = socket.socket()         
host = "127.0.0.1"
port = 80   
s.bind((host, port))  

s.listen(5)

while True:
   print("Waiting for connection")
   c, addr = s.accept()  
   print ('Got connection from', addr)
   data = c.recv(1024)
   data_string = data.decode("utf-8")
   print(data_string)
   c.send(b'HTTP/1.1 200 OK\r\n\r\nHi')
   c.close()              
   
print("Done")