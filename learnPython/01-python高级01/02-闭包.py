def test(num1):

    print("----1-----")
    def test_in(num2):
        print("-----2------")
        print(num1+num2)
    return test_in

a = test(100)
a(200)

