guest = ['jike','lorry','miek']
message1 = 'I sincerely invite '
message2 = ' to have dinner with me '

print('I found a bigger table')

guest.insert(0,'huang')
guest.insert(2,'red')
guest.append('write')

for a in guest:
    print(message1 + a + message2 )

print('Sorry, we can only invite two people')


message3 = ':Sorry, we can only invite you'

print(guest)
    
while len(guest) > 2:
    print(guest.pop() + message3)
else:
    print(guest)
    for a in guest:
        print(message1 + a + message2 )

print(guest)

del guest
 
