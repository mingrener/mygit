i = 1
num = int(input("请输入行数："))
while i<=num:
	j = 1
	while j <= i:
		print("*", end="")
		j+=1
	i +=1
	print("")
