class Restuarant():

    #初始化
    def __init__(self,reatuarant_name,cuisine_type):
        self.reatuarant_name = reatuarant_name
        self.cuisine_type = cuisine_type

    def  describe_restuarant(self):
        print('餐馆的名字：' + self.reatuarant_name)
        print('餐馆的风格：' + self.cuisine_type)

    def open_restuarant(self):
        print("餐馆正在营业")

restuarant = Restuarant('tan','tu')

restuarant.describe_restuarant()

restuarant.open_restuarant()
