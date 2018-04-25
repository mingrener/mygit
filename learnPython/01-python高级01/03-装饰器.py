def test1(fun):
    print("正在装饰1")
    def inner1():
        print("----正在验证权限1----")
        fun()
    return inner1
def test2(fun):
    print("正在装饰2")
    def inner2():
        print("----正在验证权限2----")
        fun()
    return inner2

@test1
@test2
def f1():
    print("-----f1-------")

f1()
