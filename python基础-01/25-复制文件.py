name = input("请输入要复制的文件名：")
f = open(name, "r")
a = f.read()

f.close

temp = name.split(".")
#print(name)
temp[0] = temp[0] + "[复制]"
new_name = ".".join(temp)

f = open(new_name, "w")

f.write(a)

f.close
