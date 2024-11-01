import os
def check_file(path):
    if os.path.exists(path) and os.path.isfile(path):
        return True
    return False

# 使用示例
file_path = r'D:\learning pycharm\day8\ex1.py'  # 替换为你的具体文件名
if check_file(file_path):
    print("文件存在且是一个普通文件。")
else:
    print("文件不存在或不是一个普通文件。")

import os

def check_read_permission(path):
    # 检查文件是否存在且可读
    if os.path.exists(path) and os.access(path, os.R_OK):
        return True
    return False

# 使用示例
file_path = r'D:\learning pycharm\day8\ex1.py'  # 替换为你的具体文件名
if check_read_permission(file_path):
    print("文件存在且具有读取权限。")
else:
    print("文件不存在或没有读取权限。")
