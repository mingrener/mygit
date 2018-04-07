# 定义一个全局变量
cards_infor = []
def print_menu():
	"""打印功能菜单"""
	print("="*30)
	print("       名片管理系统 V1.0")
	print("1添加名片")
	print("2删除名片")
	print("3修改名片")
	print("4查寻名片")
	print("5打印所有名片")
	print("6退出功能")
	print("="*30)
def add_cards():
	"""用于添加名片"""
	global cards_infor
	new_name = input("请输入姓名：")
	new_age= input("请输入年龄：")
	new_qq = input("请输入QQ：")
	infor = {}
	infor["name"] = new_name
	infor["age"] = new_age
	infor["qq"] = new_qq
	cards_infor.append(infor)
	#print(cards_infor)
def del_cards():
	"""用于删除名片"""
	global cards_infor
	del_name = input("请输入要删除的姓名：")
	for temp in cards_infor:
		if del_name==temp["name"]:
			cards_infor.remove(temp)
	#print(cards_infor)
def mod_cards():
	"""用于修改名片"""
	global cards_infor
	mod_name = input("请输入要修改的姓名：")
	mod_age = input("请输入要修改的年龄：")
	mod_qq = input("请输入要修改的QQ：")

	for temp in cards_infor:
		if mod_name==temp["name"]:
			temp["name"] = mod_name
			temp["age"] = mod_age
			temp["qq"] = mod_qq
	#print(cards_infor)
def find_cards():
	"""用于查找名片"""
	global cards_infor
	find_name = input("请输入要查询的姓名：")
	find_flag = 0
	for temp in cards_infor:
		if find_name==temp["name"]:
			print("%s\t%s\t%s" %(temp["name"],temp["age"],temp["qq"]))
			find_flag = 1
	if find_flag==0:
		print("查无此人")
def print_all_cards():
	"""用于打印所有的名片"""
	global cards_infor
	print("%s\t%s\t%s" %("姓名","年龄","QQ"))
	for temp in cards_infor:
			print("%s\t%s\t%s" %(temp["name"],temp["age"],temp["qq"]))
def main():
	"""用于控制所有的功能"""
	# 调用打印菜单函数
	print_menu()

	while True:
		#判断用户输入的功能
		num = int(input("请输入功能编号："))
		if num==1:
			add_cards()
		elif num==2:
			del_cards()
		elif num==3:
			mod_cards()
		elif num==4:
			find_cards()
		elif num==5:
			print_all_cards()
		elif num==6:
			break
main()
