class Restuarant():

    #初始化
    def __init__(self,reatuarant_name,cuisine_type,num = 0):
        self.reatuarant_name = reatuarant_name
        self.cuisine_type = cuisine_type
        self.number_served = num

    def  describe_restuarant(self):
        print('餐馆的名字：' + self.reatuarant_name)
        print('餐馆的风格：' + self.cuisine_type)
        print('曾经有%d人在这家餐厅就餐过：' % self.number_served)

    def open_restuarant(self):
        print("餐馆正在营业")

    def set_number_served(self,num):
        self.number_served = num

    def increment_number_served(self,num = 30):
        if self.number_served < num:
            self.number_served += 1
        else:
            print('客满')


restuarant1 = Restuarant('sun','li')
restuarant1.describe_restuarant()

restuarant1.set_number_served(12)
restuarant1.describe_restuarant()

restuarant1.increment_number_served()
restuarant1.describe_restuarant()

restuarant1.increment_number_served(10)
restuarant1.describe_restuarant()

restuarant1.open_restuarant()

