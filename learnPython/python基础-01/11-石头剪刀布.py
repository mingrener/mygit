import random
#提示并获取用户输入
player =int(input("请输入0石头 1剪刀 2布："))
comp = random.randint(0,2)
#判断输赢条件并显示结果
if (player==0 and comp ==1) or (player==1 and comp==2) or (player==2 and comp==0):
	print("你赢了...再来一局吧...")
elif player==comp:
	print("平局...洗洗手再来一局...")
else:
	print("你输了...没关系下局会赢的...")
