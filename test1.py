from tkinter import *

def printHellow() :
    print("Hi")

root = Tk()

w = Label(root, text="Python Test")
b = Button(root, text="Hello Python", command=printHellow)
c = Button(root, text="Quit", command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()
