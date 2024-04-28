import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("127.0.0.1", 8080))
tcp_server.listen(5)  # 显式指定连接请求队列的最大长度为 5
print("服务器开始监听")

conn, addr = tcp_server.accept()
print(f"接受到来自 {addr} 的连接")

while True:
    data = conn.recv(1024)
    if data == b'close':
        print("服务器已关闭")
        break
    # if not data:
    #     print("客服端已经关闭")
    #     break
    print(data)
    conn.sendall(data)

conn.close()
tcp_server.close()
