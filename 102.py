import os

def generate_index_html(directory, output_file, host_directory):
    with open(output_file, 'w') as f:
        f.write("<html>\n<head>\n<title>Index of .py Files</title>\n</head>\n<body>\n")
        f.write("<h1>Index of .py Files</h1>\n")
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, host_directory)
                    link = f"<a href='file://{file_path}'>{file}</a>"
                    f.write(f"<p>{link}</p>\n")
                    
        f.write("</body>\n</html>")

# Example usage
generate_index_html("D:/app/python/Lib", "index.html", "D:/app/python/Lib")
