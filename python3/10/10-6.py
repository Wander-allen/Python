while True:
    first_number = input('请输入一个数字：')
    if first_number == 'q':
        break
        
    second_number = input('请输入第二个数字：')
    if first_number == 'q':
        break
    
    try:
        summary = int(first_number) + int(second_number) 
    except ValueError:
        print("请重新输入整数")
    else:
        print(summary)
        print("输入'q'停止输入")
