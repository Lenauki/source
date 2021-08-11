from tkinter import *
w = Tk()

button1 = Button(w, text = '버튼1')
button2 = Button(w, text = '버튼2')
button3 = Button(w, text = '버튼3')

button1.pack(side=LEFT)
button2.pack(side=TOP)
button3.pack(side=RIGHT)

w.mainloop()
