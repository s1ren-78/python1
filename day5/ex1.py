# 定义一个 3x4 的矩阵
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 外层循环遍历行
for i in range(len(matrix)):
    # 内层循环遍历列
    for j in range(len(matrix[i])):
        # 检查元素是否为偶数
        if matrix[i][j] % 2 == 0:
            print(f"元素 {matrix[i][j]} 在位置 ({i}, {j}) 是偶数")
        else:print("其他是奇数")
