from tkinter import *
master = Tk()
whatever_you_do = "Whatever you do will be insignificante, but it is very important that you do it. \n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg ='lightgreen', font=('times', 24, 'italic'))
msg.pack()
mainloop()
