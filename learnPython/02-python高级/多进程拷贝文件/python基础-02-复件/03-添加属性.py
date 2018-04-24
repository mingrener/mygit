class Cat:
    #属性

    #方法
    def eta(self):
        print("猫仔吃鱼")

    def drink(self):
        print("猫在喝水")
#创建一个对象
tom = Cat()
#调用tom指向的对象中的方法
tom.eta()
tom.drink()
#给tom指向的对象添加了两个属性
tom.name = "汤姆"
tom.age = 40
