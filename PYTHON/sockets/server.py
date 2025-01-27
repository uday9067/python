import socket

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('172.20.10.3',55555))

s.listen()

while True:
    client, address= s.accept()
    print("connect to {}".format(address))
    client.send("you are connected".encode())
    client.close()