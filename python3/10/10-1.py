file_path = r'.\file\python.txt'


#第一次读取整个文件
file = open(file_path,'r')

if file:
    contents = file.read()
    print(contents)
file.close()

#第二次遍历文件对象
file = open(file_path,'r')

if file:
    lines = file.readlines()

    for line in lines: 
        print(line.rstrip())
file.close()

#第三次存在列表中，with快外打印
list1 = []
with open(file_path,'r') as file_object:
    lines = file_object.readlines()
    
for line in lines:
    list1.append(line.rstrip())
    
for l in list1:
    print(l)
    
