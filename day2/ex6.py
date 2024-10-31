#需求分析、代码编写、测试、维护、迭代
num1=input('请输入一个数字：')
num2=input('请输入另一个数字：')
op=input('请输入运算符号')
print('结果是',eval(f"{num1}{op}{num2}"))
#因为num1默认为字符串，需要eval来使他可被计算