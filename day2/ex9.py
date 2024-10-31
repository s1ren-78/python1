#元组,处理一次性数据
#创建之后不可修改
#元组用（）来定义 tuple函数定义
#set可变，frozenset不可变、set函数创建集合、集合自动去重
#tuple函数创建元组
obj=(1,2,3)
#obj[0] = 4,报错，因为元组不支持元素修改
new_obj=set(obj)
print(new_obj)#自动去重
new_obj_2=tuple(new_obj)
print(new_obj_2)



