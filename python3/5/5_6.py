


while 1:

    age = int(input('请输入你的年龄'))
    
    if age < 2:
        print('他是婴儿')
    elif age < 4:
        print('他正在蹒跚学步')
    elif age < 13:
        print('他是一个儿童')
    elif age < 20:
        print('他是一个青少年')
    elif age < 65:
        print('他是一个成年人')
    else:
        print('他是一个老年人')
        break
