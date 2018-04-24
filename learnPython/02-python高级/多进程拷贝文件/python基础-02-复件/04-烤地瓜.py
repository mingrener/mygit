class SweetPotato:
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []
    def __str__(self):
        return "地瓜的状态是：%s, 添加的佐料有：%s"%(self.cookedString, str(self.condiments))
    def cook(self,cookedTime):
        self.cookedLevel += cookedTime
        if self.cookedLevel<3 and self.cookedLevel>0:   self.cookedString = "生的"
        if self.cookedLevel>3 and self.cookedLevel<5:   self.cookedString = "半生不熟的"
        if self.cookedLevel>5:   self.cookedString ="熟的"
    def addCondiments(self, item):
        self.condiments.append(item)
digua = SweetPotato()
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.addCondiments("盐")
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.addCondiments("孜然")
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.addCondiments("胡椒")
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
