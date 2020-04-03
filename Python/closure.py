#闭包
def funx(x):
    def funy(y):
        return x*y
    return funy

def fun1():

    x = [5]
    def fun2():
        x[0] *= x[0]
        return x
    return fun2()


def funl():

    x = 5
    def funt():
        nonlocal x
        x *= x
        return x
    return funt()





