from tests.hw2 import test

test.main()


def power():
    num = eval(input("The number: "))
    p = eval(input("The power: "))
    a = 1
    for n in range(p):
        a = a * num

    print("'num'^'p'", a)


power()