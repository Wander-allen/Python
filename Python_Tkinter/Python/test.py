import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        self.var = tk.IntVar()
        c = tk.Checkbutton(master, text="DUANG~", variable=self.var, command=self.cb)
        c.pack()

    def cb(self):
        print("variable is", self.var.get())

master = tk.Tk()
app = Application(master=master)
tk.mainloop()