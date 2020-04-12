file_path = r'.\file\programing.txt'


with open(file_path,'w') as file_object:
    while True:
        print("输入'q'停止输入")
        name = input("你为什么喜欢编程")
        
        if name == 'q':
            break
        
        full_name = name + '\n'
        print(full_name)
        file_object.write(full_name)
    

    
