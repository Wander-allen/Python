def city_country(city,country = 'china'):
        """城市国家"""
        result = city + ',' +country
        return result


print(city_country('shenzheng'))

print(city_country('shanghai'))

print(city_country('xini',"US"))
