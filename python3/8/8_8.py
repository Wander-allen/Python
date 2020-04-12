def make_album(special,num):
        "函数返回值字典"
        albun = {}
        albun[special] = num
        return albun

while True:
        special = input("请输入你的专辑：")
        print("输入'q'结束")
        if special == 'q':
                break
        
        num = int(input("请输入你的专辑数量："))
        print("输入'q'结束")
        if special == 'q':
                break
        
        print(make_album(special,num))



