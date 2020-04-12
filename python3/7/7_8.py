sandwitch_orders = ['red','yellow','blue']
finished_sandwiches = []

while sandwitch_orders:
    current_sandwiches = sandwitch_orders.pop()
    print('i made your ' + current_sandwiches +' sandwitch')
    finished_sandwiches.append(current_sandwiches)

for sandwiches in finished_sandwiches:
    print(sandwiches)
    
