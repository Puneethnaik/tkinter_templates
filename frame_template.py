from tkinter import *
class CustomFrame(Frame):
    def __init__(self, title, row, column, parent=None):
        Frame.__init__(self, parent)
        self.grid(row = row, column = column)
        self.title = title
        #set frame state variables
        self.state = 42
        self.make_widgets()
    def make_widgets(self):
        widget = Button(self, text = "Hello Frame" + self.title)
        widget.pack(side=LEFT)
