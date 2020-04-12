persons = {
    'zhao':[2,4,6],
    'qian':[2,4,6],
    'wu':[2,4,6],
    'li':[2,4,6],
    'chen':[2,4,6]
    }

for name,nums in persons.items():
    print('\n',name)
    for num in nums:
        print('\t',num)
