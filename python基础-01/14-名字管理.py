#打印功能
print("="*30)
print("       名字管理系统 V1.0")
print("1添加姓名")
print("2删除姓名")
print("3修改姓名")
print("4查寻姓名")
print("5退出功能")

print("="*30)
names = []
while True:
	#判断用户输入的功能
	num = int(input("请输入功能编号："))
	if num==1:
		new_name = input("请输入姓名：")
		names.append(new_name)
		print(names)
	elif num==2:
		
		del_name = input("请输入姓名：")
		names.remove(del_name)
		print(names)
	elif num==3:
		
		mod_name = input("请输入要修改的姓名：")
		i = 0
		while i<=(len(names)-1):
			if names[i]==mod_name:
				new_name = input("请输入新的姓名：")
				names[i] = new_name
				break
			i+=1
		print(names)
	elif num==4:
		find_name = input("请输入姓名：")
		if find_name in names:
			print("找到了")
		else:
			print("查无此人")
	elif num==5:
		break
