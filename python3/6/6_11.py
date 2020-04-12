cities = {
    'shenzhen':{
        'country':'china',
        'population':'1.2万',
        'fact':'biggr',
        },
    
    'chongqing':{
        'country':'china',
        'population':'8万',
        'fact':'biggr',
        },

    'shagnhai':{
        'country':'china',
        'population':'9万',
        'fact':'biggr',
        },
    
    }

for city,info in cities.items():
    print('\nCity_name:'+city)
    print('\tcountry:'+info['country'])
    print('\tpopulation:'+info['population'])
    print('\tfact:'+info['fact'])
