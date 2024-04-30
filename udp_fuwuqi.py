import socket
host='127.0.0.1'
port=8080
upd_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
upd_server.bind((host,port))
print("UPD server is working...")
while True:
    data,addr = upd_server.recvfrom(1024)
    print(f"received {data} from {addr[0]}:{addr[1]}")
    if data==b'close':
        print('server closed')
        break
    upd_server.sendto(data,addr)
upd_server.close()
