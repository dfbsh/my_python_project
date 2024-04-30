import socket
host="127.0.0.1"
port=8080
upd_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:#记住True不是true
    send_data=input("please input data or 'close' command to send:")
    upd_client.sendto(send_data.encode(),(host,port))
    if send_data == 'close':
        print("send close")
        break
    info=upd_client.recv(1024).decode()
    print(f"recieve form {info}")

upd_client.close()
