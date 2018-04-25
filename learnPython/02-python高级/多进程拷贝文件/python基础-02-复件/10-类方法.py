class Game(object):
    #类属性
    num = 0
    def __init__(self):
        self.name = "11"

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100
game = Game()

Game.add_num()

print(Game.num)
