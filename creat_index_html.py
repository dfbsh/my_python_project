import os
import sys

def find_python_lib_path():
    # 获取当前正在使用的 Python 解释器的路径
    python_executable = sys.executable
    
    # 获取 Python 安装目录的父目录
    python_install_dir = os.path.dirname(python_executable)
    
    # 构建 lib 文件夹的路径
    lib_dir = os.path.join(python_install_dir, 'lib')
    
    return lib_dir


def generate_html(directory):
    # 获取目录下的所有.py文件
    py_files = [file for file in os.listdir(directory) if file.endswith('.py')]
    
    # 生成HTML内容
    html_content = "<html><head><title>Python Files Index</title></head><body>"
    html_content += "<h1>Python Files Index</h1>"
    html_content += "<ul>"
    for py_file in py_files:
        # 生成文件链接
        file_path = os.path.join(directory, py_file)
        link = f'<a href="file://{file_path}">{py_file}</a>'
        html_content += f"<li>{link}</li>"
    html_content += "</ul></body></html>"
    
    # 将HTML内容写入index.html文件
    with open('index.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    python_lib_path = find_python_lib_path()
    print("Python安装目录中lib文件夹的路径：", python_lib_path)
    # 指定目录路径
    directory_path = python_lib_path
    
    # 生成HTML文件
    generate_html(directory_path)
    print("已经生成index.html文件，请前往查看")
