def greet(name):
    return f"Hello, {name}!"

# 调用函数
print(greet("Alice"))  # 输出: Hello, Alice!

print(greet('sam'))

def add(a, b):  # 定义一个函数名为 add，接受两个参数 a 和 b
    result = a + b  # 计算 a 和 b 的和
    return result  # 返回计算结果

print(add(4,8))

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # 输出: Hello, Alice!
print(greet("Bob", "Hi"))  # 输出: Hi, Bob!


# 使用 del 删除函数
#del greet

# 尝试调用已删除的函数会引发错误
#try:
#    print(greet("Alice"))  # 这会引发 NameError，因为 greet 不再被定义
#except NameError as e:
 #   print(e)  # 输出: name 'greet' is not defined

