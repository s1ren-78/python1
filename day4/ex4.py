#语句嵌套尽量不超过三层
number=100
if number < 100:
    if number % 7 == 0:
         pass

# 创建一个二维列表
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# 遍历二维列表
for i in range(len(matrix)):  # 外层循环遍历行
    for j in range(len(matrix[i])):  # 内层循环遍历列
        print(matrix[i][j], end=' ')
    print()