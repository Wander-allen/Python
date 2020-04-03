def fun1():
    'Inline 内嵌函数'
    print('fun1()正在被调用。。。')
    def fun2():
       print('fun2()正在被调用。。。')
    fun2()
