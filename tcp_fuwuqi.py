import socket

tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.bind('127.0.0.1','12345')
tcp_server.listen()
print("sever starts listen")
a,b=tcp_server.accept()
print(f"accept from {b}")
while True:
    data=a.recv(1024)
    if data==b'close':
        print("sever is close")
        break
    print(data)
    a.sendall(data)
a.close()
tcp_server.close()


