#选择for循环的场景：
#你知道要遍历的序列的长度。
#你想要对序列中的每个元素执行相同的操作。
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

my_dict = {'name': 'Alice', 'age': 30, 'city': 'Beijing'}

for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

my_dict = {'name': 'Alice', 'age': 30, 'city': 'Beijing'}
for key, value in my_dict.items():
    print(f"{key}: {value}")