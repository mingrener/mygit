'''
func = lambda x,y:x+y
a = func(11,22)
print(a)
'''

infors = [{"name":"laowang","age":"18"},{"name":"aaowang","age":"14"},{"name":"vaowang","age":"8"}]
infors.sort(key = lambda x:x["name"])
print(infors)
