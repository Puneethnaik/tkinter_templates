from tkinter import *
root = Tk()

labelName = Label(root, text = "Name : ")
labelName.grid(row = 0, sticky = 'e')

labelPass = Label(root, text = "Password : ")
labelPass.grid(row = 1, sticky = 'e')

name = Entry(root)
name.grid(row = 0, column = 1)
password = Entry(root)
password.grid(row = 1, column = 1)

c = Checkbutton(root, text = "keep me logged in.")
c.grid(columnspan = 2)

root.mainloop()