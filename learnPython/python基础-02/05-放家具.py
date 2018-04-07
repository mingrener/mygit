class home():
    def __init__(self, new_area, new_type, new_addr):
        self.area = new_area
        self.type = new_type
        self.addr = new_addr
        self.left_area = new_area
        self.items = []
    def __str__(self):
        msg = "房子的总面积是：%d，当前面积是：%d, 户型是：%s, 地址是：%s"%(self.area, self.left_area, self.type, self.addr)
        msg += "房子里的家具有：%s"%(self.items)
        return msg
    def addItem(self, item):
        self.left_area -= item.get_area()
        self.items.append(item.get_name())
class bed():
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area
    def get_area(self):
        return self.area
    def get_name(self):
        return self.name
fangzi = home(130, "三室一厅", "南京市 鼓楼区")
print(fangzi)
bed1 = bed("婴儿床", 3)
fangzi.addItem(bed1)
print(fangzi)
