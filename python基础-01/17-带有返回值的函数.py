#定义一个获取温度的函数
def measure_temperature():
	temperature = 22
	return temperature
#定义一个转换单位的函数
def convert_temperature(temperature):
	new_temp = temperature + 180
	return new_temp
#调用
temperature = measure_temperature()
print("现在的华氏温度是：%d"%convert_temperature(temperature))
