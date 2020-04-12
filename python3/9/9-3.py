class User:

    def __init__(self,first,last,*user):
        self.first_name = first
        self.last_name = last
        self.userInfo = user

    def descirbe_user(self):
        print(self.first_name + ' ' + self.last_name)
        if self.userInfo:
            print(self.userInfo)

    def greet__user(self):
        print('hello '+ self.first_name + ' ' + self.last_name)
        
user1 = User('zhao','qian')
user1.descirbe_user()
user1.greet__user()

user2 = User('sun','li','you are beautiful')
user2.descirbe_user()
user2.greet__user()

user3 = User('zhou','wu','hehe')
user3.descirbe_user()
user3.greet__user()

user4 = User('zhen','wan')
user4.descirbe_user()
user4.greet__user()
        
