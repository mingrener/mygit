class Test():
    def __init__(self):
        self.__num = 100
    @property
    def num(self):
        print("get")
        return self.__num
    @num.setter
    def num(self,num):
        print('set')
        self.__num = num
a = Test()
a.num = 300
print(a.num)
