list_name=['name1','name2','name3']
list_sn=[111,222,333]

name_sn={list_name[0]:list_sn[0],list_name[1]:list_sn[1],list_name[2]:list_sn[2]}
print(name_sn)
print(name_sn.items())#访问所有键
print(name_sn.get('name1'))
for key , value in name_sn.items():#遍历字典，字典内置函数
    print(key)
    print(value)

print(name_sn.popitem())#移除最后一项
print(name_sn)

#print(name_sn.pop('name1'))#删键
#print(name_sn)
#for key, value in name_sn.items():
   # print(key)  # 缩进与 for 同级
   #print(value)  # 缩进与 for 同级
print(name_sn.popitem())#移除最后一项
print(name_sn)
print(name_sn.popitem())#移除最后一项
print(name_sn)
#print(name_sn.popitem())#移除最后一项
#print(name_sn)#空字典没法移除，会报错