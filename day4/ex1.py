sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1#累加
print(sum)
password = "yourpassword"
input_password = ""
while input_password != password:#循环为真时，代码不会被执行
    input_password = input("请输入密码：")
print("密码正确！")

