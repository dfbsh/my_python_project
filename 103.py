import socket
import os

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode("utf-8")
    request_lines = request_data.split("\r\n")
    if len(request_lines) > 0:
        filename = request_lines[0].split()[1]
        if filename == "/":
            filename = "/index.html"
        
        filename = "." + filename
        
        if os.path.exists(filename) and os.path.isfile(filename):
            with open(filename, "rb") as f:
                content = f.read()
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers += "Content-Length: {}\r\n".format(len(content))
            response_headers += "\r\n"
            response = response_headers.encode("utf-8") + content
        else:
            response = b"HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"
        
        client_socket.sendall(response)

def main():
    #host = "192.168.43.97"
    host="127.0.0.1"
    port = 8080
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            handle_request(client_socket)
            client_socket.close()
    except KeyboardInterrupt:
        print("Server is shutting down")
        server_socket.close()

if __name__ == "__main__":
    main()
