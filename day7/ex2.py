# 写入 UTF-8 编码文件
# with open('utf8_file.txt', 'w', encoding='utf-8') as f:
#     f.write('Hello, 世界！')  # 写入包含中文字符的内容
# 读取 UTF-8 编码文件
with open('utf8_file.txt', 'r', encoding='utf-8') as f:
    content = f.read(1)
    print(content)  # 输出: Hello, 世界！
# 写入 GBK 编码文件
with open('gbk_file.txt', 'w', encoding='gbk') as f:
    f.write('你好，世界！')  # 写入包含中文字符的内容
# 读取 GBK 编码文件
with open('gbk_file.txt', 'r', encoding='gbk') as f:
    content = f.read()
    print(content)  # 输出: 你好，世界！
# 尝试用 UTF-8 读取 GBK 编码的文件

#
