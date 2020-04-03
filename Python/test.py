def MyFirstFunction():
        #'骄傲的我写的第一个程序'
	print('只是我创建的第一程序：')
	print('我表示很鸡冻......')
	print('在此我要感谢父老详情对我的厚爱')

def Add(num1,num2):
        '这是一个加法函数：return value -> num1 + num2'
        result = num1+num2
        print(result)
        
import random
        
def PlayPlane():
        '这是一个打飞机游戏'
        print('这是一个打飞机游戏！！！')
        result = random.randint(0,100)
        temp = int(input('请输入一个数字：'))
        guess = 5
        while result != temp and guess > 0:
                if(temp > result):
                        print('大哥，你输入的数字太大')
                elif(temp < result):
                        print('大哥，你输入的数字太小')
                temp = int(input('请输入一个数字：'))
                guess -= 1
        if guess == 0:
                print('The right Value :',result,' look up you')
                print('you are lower ,game over!!!!')
        else:       
                print('good luck,youare right')

def TestFun(name):
        '函数定义过程中的name是叫形参'#文本介绍，可以用help(TestFun)或TestFun.__doc__打开
        #因为Ta只是一个形式，表示占据一个参数位置
        print('传进来的'+ name + '叫做实参，应为Ta视具体参数值')


def SaySome(name = 'tanminhang',world='charge the world'):
        "关键字参数，可以添加默认值，SaySome(world = '改变世界',name = '谈岷杭')"
        print(name+'->'+world)

def TestArgPara(*paras):
        '这是一个可变函数参数测试'
        print('参数的长度是：',len(paras))
        print('第二个参数是：',paras[1])

def TestArgParaTwo(*paras,exp = 8):
        '这是两个可变函数参数测试'
        print('参数的长度是：',len(paras),exp)
        print('第二个参数是：',paras[1])



                
	


