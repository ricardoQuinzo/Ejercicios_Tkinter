from Tkinter import*
master = Tk()

def var_states():
    print "masculino: ",var1.get()
    print "femenino: ", var2.get()

Label(master, text =" Indicar el sexo: ").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text=" Masculino", variable=var1).grid(row=1,sticky=W)
var2 = IntVar()
Checkbutton(master, text=" Femenino", variable=var2).grid(row=2,sticky=W)
Button(master, text ='Quit',command = master.quit).grid(row=3,sticky=W, padx=4)
Button(master, text ='Show',command = var_states).grid(row=4,sticky=W, padx=4)
mainloop()


