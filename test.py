from tkinter import *

def pin():
    global inputq
    pinq = Tk()
    x = (pinq.winfo_screenwidth() - pinq.winfo_reqwidth()) / 2
    y = (pinq.winfo_screenheight() - pinq.winfo_reqheight()) / 2
    pinq.wm_geometry("+%d+%d" % (x, y))
    pinq.resizable(width=False, height=False)
    pinq.title('Pin')
    pinq.geometry('190x300')
    pinq['bg'] = 'cyan'
    pinw = '116596'
    inputq = ''

    num = Text(pinq, width=17, height=1)
    num.configure(state='disabled')
    num.place(x=10, y=10)

    def cancel():
        pinq.destroy()

    def clear():
        global inputq
        inputq = ''
        num.configure(state='normal')
        num.delete(1.0, END)
        num.configure(state='disabled')

    def add(n):
        global inputq
        inputq += str(n)
        num.configure(state='normal')
        num.delete(1.0, END)
        num.insert(INSERT, inputq)
        num.configure(state='disabled')
        if inputq == pinw:
            print('niceeee')

    Button(pinq, command=lambda: add(1), text='1', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=40)
    Button(pinq, command=lambda: add(2), text='2', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=40)
    Button(pinq, command=lambda: add(3), text='3', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=40)
    Button(pinq, command=lambda: add(4), text='4', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=105)
    Button(pinq, command=lambda: add(5), text='5', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=105)
    Button(pinq, command=lambda: add(6), text='6', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=105)
    Button(pinq, command=lambda: add(7), text='7', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=170)
    Button(pinq, command=lambda: add(8), text='8', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=170)
    Button(pinq, command=lambda: add(9), text='9', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=170)
    Button(pinq, command=lambda: add(0), text='0', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=235)
    Button(pinq, command=clear, text='Reset', width=5, bg='light grey', activebackground='grey', height=3).place(
        x=10, y=235)
    Button(pinq, command=cancel, text='Cancel', width=5, bg='light grey', activebackground='grey', height=3).place(
        x=130, y=235)
    pinq.mainloop()
pin()