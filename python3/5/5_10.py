
current_users = ['admin','tan','huang','liu','chen']

new_users = ['zhao','qian','tan','sun','liu']

#转成小写重新排序
lower_current_users = [current_user for current_user in current_users]

lower_current_users.sort()

print(lower_current_users)

lower_new_users = [new_user for new_user in new_users]

lower_new_users.sort()

print(lower_new_users)


for lower_new_user in lower_new_users:
    if lower_new_user in lower_current_users:
        print(lower_new_user,'and its other forms are already acount,Please change it')
    else:
        print('you can use it')



