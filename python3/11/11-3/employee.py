class Employee():
    """一个存储名、姓、和年薪的类"""
    def __init__(self,name,surname,salary = 5000):
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_raise(self):
        return self.salary

        
        
