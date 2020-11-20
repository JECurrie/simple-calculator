from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

def myClick():
	myLabel = Label(root, text="Hi")
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)

#root window
myButton.pack()



root.mainloop()