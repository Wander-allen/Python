def sandwitch_show(*food):
    "传递任意实参"
    print("\nsandWitch need the flowing topping:")
    for topping in food:
        print("-"+topping)


sandwitch_show("red","white","blue")

sandwitch_show("red","white","blue",'bluck')
