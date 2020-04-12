
users = ['admin','tan','huang','liu','chen']

if users:
    for user in users:
        if user == 'admin':
            print('hello admin,wolud you like to see a status reports?')
        else:
            print('hello ' + user + ' thank you for logging in again')
    
else:
    print('we need to find some users')

