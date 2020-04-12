response = {}

active = True

while active:
    name = input('请输入你的名字：')
    city = input('请输入你最喜欢的城市')
    
    response[name] = city

    repet = input('还需要继续吗？yes\\no')

    if repet.lower() == 'no':
        active = False
        
print('调查结束')

for name,city in response.items():
    print(name + '最喜欢的城市是' +city)
