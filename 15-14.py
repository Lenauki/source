from tkinter import *

window = Tk()
window.geometry("200x200")

upFrame = Frame(window)
upFrame.pack()
downFrame = Frame(window)
downFrame.pack()

editBox = Entry(upFrame, width= 10, bg = 'green')
editBox.pack(padx = 20, pady= 20)

listbox = Listbox(downFrame, bg = 'red')
listbox.pack()

listbox.insert(END,'one')
listbox.insert(END,'two')

window.mainloop()