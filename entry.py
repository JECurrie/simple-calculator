from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()

def myClick():
	myLabel = Label(root, text=e.get())
	myLabel.pack()

myButton = Button(root, text="Enter Your Name: ", command=myClick)

#root window
myButton.pack()



root.mainloop()