favorites_places = {
    'zhao':['china','us','russia'],
    'qian':['japen','english','russia'],
    'sun':['us','puzze','russia'],
    }

for name,value in favorites_places.items():
    print('\n',name,'favorite country is')
    for country in value:
        print('\t',country)
