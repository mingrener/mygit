class Animal:
    def eat(self):
        print("----吃------")
    def sleep(self):
        print("----睡------")
    def run(self):
        print("----跑------")
class Dog(Animal):

    def bark(self):
        print("-----汪汪叫----")

dog = Dog()
dog.eat()
