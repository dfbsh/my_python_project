import socket  # 导入 socket 模块
import os  # 导入 os 模块

def handle_request(client_socket):
    # 处理客户端请求的函数
    request_data = client_socket.recv(1024).decode("utf-8")  # 接收客户端发送的数据并解码
    request_lines = request_data.split("\r\n")  # 将请求数据按行分割
    
    if len(request_lines) > 0:
        filename = request_lines[0].split()[1]  # 获取请求中的文件名
        if filename == "/":
            filename = "/index.html"  # 如果文件名为根目录，则默认为 index.html
        
        filename = "." + filename  # 将文件名转换为相对路径
        
        # 判断请求的文件是否存在并且是一个文件
        if os.path.exists(filename) and os.path.isfile(filename):
            with open(filename, "rb") as f:
                content = f.read()  # 读取文件内容
            response_headers = "HTTP/1.1 200 OK\r\n"  # 构建响应头
            response_headers += "Content-Length: {}\r\n".format(len(content))
            response_headers += "\r\n"
            response = response_headers.encode("utf-8") + content  # 构建完整的响应
        else:
            response = b"HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"  # 如果文件不存在，返回404错误
        
        client_socket.sendall(response)  # 将响应发送给客户端

def main():
    #host = "192.168.43.97"我自己电脑的ip地址
    # 设置服务器的主机和端口
    host = "127.0.0.1"
    port = 8080
    
    # 创建套接字并绑定主机和端口
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")  # 输出服务器启动信息
    print("请在浏览器中打开   127.0.0.1:8080   即可查看到index.html文件")
    
    try:
        # 循环等待客户端连接
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")  # 输出客户端连接信息
            handle_request(client_socket)  # 处理客户端请求
            client_socket.close()  # 关闭客户端连接
    except KeyboardInterrupt:
        print("Server is shutting down")  # 在收到键盘中断信号时关闭服务器
        server_socket.close()  # 关闭服务器套接字

if __name__ == "__main__":
    main()  # 执行主函数
    print("请在浏览器中打开   127.0.0.1   即可查看到index.html文件")
