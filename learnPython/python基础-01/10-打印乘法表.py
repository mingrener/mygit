i = 1
#num = int(input("请输入行数："))
while i<=9:
	j = 1
	while j <= i:
		print("%d*%d=%d\t" %(i,j,i*j),end="")
		j+=1
	i +=1
	print("")
