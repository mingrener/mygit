#打印功能
print("="*30)
print("       名片管理系统 V1.0")
print("1添加名片")
print("2删除名片")
print("3修改名片")
print("4查寻名片")
print("5打印所有名片")
print("6退出功能")

print("="*30)
cards_infor = []
while True:
	#判断用户输入的功能
	num = int(input("请输入功能编号："))
	if num==1:
		new_name = input("请输入姓名：")
		new_age= input("请输入年龄：")
		new_qq = input("请输入QQ：")
		infor = {}
		infor["name"] = new_name
		infor["age"] = new_age
		infor["qq"] = new_qq
		cards_infor.append(infor)
		#print(cards_infor)
	elif num==2:
		
		del_name = input("请输入要删除的姓名：")
		for temp in cards_infor:
			if del_name==temp["name"]:
				cards_infor.remove(temp)
		#print(cards_infor)
	elif num==3:
		mod_name = input("请输入要修改的姓名：")
		mod_age = input("请输入要修改的年龄：")
		mod_qq = input("请输入要修改的QQ：")

		for temp in cards_infor:
			if mod_name==temp["name"]:
				temp["name"] = mod_name
				temp["age"] = mod_age
				temp["qq"] = mod_qq
		#print(cards_infor)
		
	elif num==4:
		find_name = input("请输入要查询的姓名：")
		find_flag = 0
		for temp in cards_infor:
			if find_name==temp["name"]:
				print("%s\t%s\t%s" %(temp["name"],temp["age"],temp["qq"]))
				find_flag = 1
		if find_flag==0:
			print("查无此人")
	elif num==5:
		print("%s\t%s\t%s" %("姓名","年龄","QQ"))
		for temp in cards_infor:
				print("%s\t%s\t%s" %(temp["name"],temp["age"],temp["qq"]))
	elif num==6:
		break
