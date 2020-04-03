#old_price = float(input('请输入原价：'))
#rate = float(input('请输入折扣率：'))

def Discounts(price, rate):
        """Local variable and Global variable,不要在函数内部试图修改全局变量
           如果要使用，使用关键字Glbal """
        final_price = price * rate
        global old_price
        print('这里试图打印全局变量old_price',old_price)
        old_price = 50;
        print('修改后的old_price1',old_price)
        return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = Discounts(old_price,rate)
print('修改后的old_price1',old_price)
print('打折扣的价格是', new_price)
