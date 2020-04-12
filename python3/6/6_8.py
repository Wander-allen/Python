pet1 = {
    'ahuang':['dog','zhao'],
    }

pet2 ={
    'alan':['fish','qian'],
    }

pet3 ={
    'alv':['cat','sun'],
    }

pet4 ={
    'atian':['fish','zhou'],
    }

pets = [pet1,pet2,pet4,pet4]

for pet in pets:
    print('\n' , pet.keys())
    for info in pet.values():
        print('\t', info)
