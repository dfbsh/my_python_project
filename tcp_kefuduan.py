import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(('127.0.0.1', 8080))

while True:
    send_data = input("请输入数据或输入 'close' 命令以关闭连接：")
    tcp_client.sendall(send_data.encode())

    if send_data.lower() == "close":
        print("正在关闭连接...")
        break

    info = tcp_client.recv(1024).decode()
    print("接收到的数据：", info)

tcp_client.close()
