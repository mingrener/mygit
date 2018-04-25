def test1(fun):
    print("正在装饰1")
    def inner1(*args, **kwargs):
        print("----正在验证权限1----")
        ret = fun(*args,**kwargs)
        return ret
    return inner1

@test1
def f1(a,b):
    print("-----f1-%d--%d----"%(a,b))

f1(11,22)
