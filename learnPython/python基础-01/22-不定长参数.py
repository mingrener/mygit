def sum_nums(a,b,*args):
	c = a+b
	result = 0
	for item in args:
		result+=c
	print("result = %d"%result)
sum_nums(12,13,14,15,16)

