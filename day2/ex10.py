#字典如何处理映射类型的数据
#映射是可变类型，每一个元素可以增加减少,只有字典
#字典里的一个元素由必须得键和可能得空值组成
#键不能重复、列表字典不能作为键
phonebook = {'Alice': '12345678', 'Bob': '98765432'}

# 添加新的联系人
phonebook['Charlie'] = '5551212'
ex_1=phonebook['Charlie']
print(ex_1)

# 查询电话号码
print(phonebook['Alice'])
print(phonebook['Charlie'])