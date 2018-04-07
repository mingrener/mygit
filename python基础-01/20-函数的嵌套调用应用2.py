def sum_3_nums(num1,num2,num3):
	result = num1+num2+num3
	return result
def average_3_nums(a,b,c):
	result = sum_3_nums(a,b,c)/3
	return result
a = int(input("请输入第1个数："))
b = int(input("请输入第2个数："))
c = int(input("请输入第3个数："))
#sum = sum_3_nums(a,b,c)
#print("三个数的和是：%d"%sum)
averge = average_3_nums(a,b,c)
print("三个数的平均值是：%d"%averge)
