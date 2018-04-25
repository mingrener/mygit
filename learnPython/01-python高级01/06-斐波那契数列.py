def createNum(num):
    a,b=0,1
    for i in range(num):
        yield b
        a,b=b,a+b
for n in createNum(10):
    print(n)
