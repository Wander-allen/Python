file_path = r'.\file\python.txt'


#第三次存在列表中，with快外打印
list1 = []
with open(file_path,'r') as file_object:
    lines = file_object.readlines()
    
for line in lines:
    line = line.replace('Python','c')#将Pyhon替换成c
    list1.append(line.rstrip())
    
for l in list1:
    print(l)
    
