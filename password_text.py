# import getpass
#
# print("Please enter your password")
# # 获取用户输入的密码
# password = getpass.getpass("请输入密码：")
#
# # 打印用户输入的密码
# print("您输入的密码是:", password)
# 将字符串转换为字节串（使用默认的 UTF-8 编码）
string = "Hello, world!"
byte_string = string.encode()

# 打印转换后的字节串及其类型
print(byte_string)
print(type(byte_string))
