try:
    #try语句如果出现异常，后面的语句不会被执行
    sun = 1+'i'
    f = open('nnjnj.txt')
    print(f.read())
    f.close()
    
#except同时对多个异常进行处理  
except OSError as reason:
    print('文件出错啦、你错误的的源影视：'+str(reason))
except TypeError as reason:
    print('类型出错啦、你错误的的源影视：'+str(reason))

#无论如何都会执行的代码
finally:
    print('无论如何都会执行的代码')
