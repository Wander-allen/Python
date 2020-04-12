content = ''
dogs_path = r'.\file\dogs.txt'
cats_path = r'.\file\cats.txt'

try:
    with open(cats_path,'r') as file_object:
        content = file_object.read()
except FileNotFoundError:
    #print("cats.txt 不存在")
    pass #不做任何处理
else:
    print(content)
    try:
        with open(dogs_path,'r') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        #print("dogs.txt 不存在")
        pass
    else:
        print(content)
    
