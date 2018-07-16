from tkinter import *

root = Tk()

one = Label(root, text = "One", bg = "red", fg = "white")
one.pack()

two = Label(root, text = "Two", bg = "green", fg = "white")
two.pack()

three = Label(root, text = "three", bg = "red", fg = "green")
three.pack()



root.mainloop()