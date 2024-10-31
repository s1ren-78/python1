list_name=['name1','name2','name3']
list_sn=[111,222,333]

name_sn={list_name[0]:list_sn[0],list_name[1]:list_sn[1],list_name[2]:list_sn[2]}

print(name_sn.setdefault('name4',444))#若没有，则添加的逻辑
print(name_sn.items())