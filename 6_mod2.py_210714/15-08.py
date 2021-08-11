from tkinter import *

window = Tk()

Label1 = Label(window, text="This is MySQL을")
Label2 = Label(window, text="열심히", font=("나눔고딕",30),fg='blue')
Label3 = Label(window, text="공부중입니다",bg='yellow',width=20,height=5,anchor=SE)

Label1.pack()
Label2.pack()
Label3.pack()

window.mainloop()