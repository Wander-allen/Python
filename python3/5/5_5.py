alien  = ['green','yellow','red']

colour = input('请输入你的颜色')

if colour == alien[0]:
    print('玩家获得5个点')
elif colour == alien[1]:
    print('玩家获得10个点')
elif colour == alien[2]:
    print('玩家获得15个点')

