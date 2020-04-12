class User:

    def __init__(self,first,last,login):
        self.first_name = first
        self.last_name = last
        self.login_attempts = login

    def descirbe_user(self):
        print(self.first_name + ' ' + self.last_name)
        print('login_attempts ' + str(self.login_attempts))


    def greet__user(self):
        print('hello '+ self.first_name + ' ' + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self,first,last,login,*privileges):
        super().__init__(first,last,login)
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
        
user1 = Admin('zhao','qian',10,['can add post','can delete post','can ban user'])
user1.descirbe_user()
user1.show_privileges()

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


        
