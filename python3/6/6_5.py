rivers = {
    'nile':'egypt',
    'changjiang':'china',
    'hunaghe':'china',
    }

for river,country in rivers.items():
    print('The '+river.title()+'runs through '+ country.title())

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

    
