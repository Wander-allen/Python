def city_country(city,country):
    """返回City, country这样的字符串"""
    full_name = city + ', ' + country
    return full_name.title()

def city_country_population(city,country,population = ""):
    """返回City, Country - population XXX这样的字符串"""
    if population:
        full_name = city + ', ' + country + ' - Population ' + population
    else:
        full_name = city + ', ' + country
    return full_name.title()
    
