import json

favorite_number_path = r".\file\favorte_number.json"

number = int(input("输入一个你喜欢的数字："))

with open(favorite_number_path,'w') as file_object:
    json.dump(number,file_object)
    
with open(favorite_number_path,'r') as file_object:
    number2 = json.load(file_object)


print("I know your favorite number! It's %d" %number2)    
