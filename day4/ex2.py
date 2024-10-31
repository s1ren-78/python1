# 计算1到10的平方，并将结果存入列表
squares = []
for i in range(1, 11):
    square = i * i
    squares.append(square)

print(squares)  # 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

fruits = ["apple", "banana", "cherry"]
index = 0

while index < len(fruits):
    fruit = fruits[index]
    print(fruit)
    index += 1