from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Joan Currie.")
myLabel3 = Label(root, text="My name is 3.")
myLabel4 = Label(root, text="My name is 4.")

#root window
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=2)
myLabel4.grid(row=1, column=3)

root.mainloop()