from tkinter import *

longtext = """
Label 可以显示多行文本，你可以直接使用换行符
或使用 wraplength 选项来实现。当文本换行的时
候，你可以使用 anchor 和 justify 选项来使得
文本如你所希望的显示出来。
"""

master = Tk()

v = StringVar()

# w = Label(master, text = longtext, font = "Consolas", fg = "red", justify = LEFT)
w = Label(master, textvariable = v, font = "Consolas", fg = "red", justify = RIGHT)
v.set("This is textvariable string")
w.pack()

var = 5
def callback():
    global var
    #var = 5
    var = var + 1
    print("this is a callback %s" % str(var))  
    v.set(str(var))
    k.config(relief = SUNKEN)

k = Button(master, text = "gan", command = callback, padx = 10, pady = 0, height  = 2, width = 4, anchor = "w", justify = RIGHT)
# k = Button(w, text = "gan", command = callback, padx = 10, pady = 0, height  = 2, width = 4, anchor = "w", justify = RIGHT)
k.pack()

var = IntVar()

h = Checkbutton(master, text = "我是美女", variable = var)
h.pack()

v = StringVar()
v.set("T")

i = Checkbutton(master, text = "你有女朋友吗", variable = v, onvalue = "T", offvalue = "F")
i.pack()




mainloop()
