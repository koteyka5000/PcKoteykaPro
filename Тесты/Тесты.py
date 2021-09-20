from tkinter import *

valuesRoot = Tk()
valuesRoot.geometry('300x200')
valuesRoot['bg'] = 'cyan'
valuesRoot.title('Koteyka Test')
valuesRoot.resizable(0, 0)
x = (valuesRoot.winfo_screenwidth() - valuesRoot.winfo_reqwidth()) / 2
y = (valuesRoot.winfo_screenheight() - valuesRoot.winfo_reqheight()) / 2
valuesRoot.wm_geometry("+%d+%d" % (x, y))

textInX = Entry(valuesRoot, width=30)
textInX.place(x=90, y=10)

textInY = Entry(valuesRoot, width=30)
textInY.place(x=90, y=40)

Label(text='X:', fg='blue', bg='cyan', font='Arial 14').place(x=5, y=5)
Label(text='Y:', fg='blue', bg='cyan', font='Arial 14').place(x=5, y=35)


Button(valuesRoot, text='Готово', bg='yellow', width=20, activebackground='cyan', command=).place(x=130, y=160)


def enter():
    x = textInX.get()
    y = textInY.get()
    try: x, y = int(x), int(y)
    except: Label(valuesRoot, text='ВВЕДИТЕ ЧИСЛА!', foreground='red', bg='cyan').place(x=10, y=160)
    else:
        valuesRoot.destroy()
        return x, y


Button(valuesRoot, text='Готово', bg='yellow', width=20, activebackground='cyan', command=enter).place(x=130, y=160)

valuesRoot.mainloop()
