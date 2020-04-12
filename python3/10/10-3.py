file_path = r'.\file\guest.txt'


with open(file_path,'w') as file_object:
    name = input("请输入你的名字：")
    file_object.write(name)
    

    
