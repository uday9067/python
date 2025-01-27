import socket

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.20.10.3',55555))
massage = s.recv(1024)
s.close()

print(massage.decode())