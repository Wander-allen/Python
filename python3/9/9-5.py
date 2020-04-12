class User:

    def __init__(self,first,last,login,*user):
        self.first_name = first
        self.last_name = last
        self.userInfo = user
        self.login_attempts = login

    def descirbe_user(self):
        print(self.first_name + ' ' + self.last_name)
        print('login_attempts ' + str(self.login_attempts))
        if self.userInfo:
            print(self.userInfo)

    def greet__user(self):
        print('hello '+ self.first_name + ' ' + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = User('zhao','qian',10)
user1.descirbe_user()

user1.increment_login_attempts()
user1.descirbe_user()

user1.increment_login_attempts()
user1.descirbe_user()

user1.increment_login_attempts()
user1.descirbe_user()

user1.increment_login_attempts()
user1.descirbe_user()

user1.reset_login_attempts()
user1.descirbe_user()

user1.greet__user()


        
