
from tkinter import *
from tkinter import messagebox as mb


class Person:
    def __init__(self, name, id, password, friend):
        self.name = name
        self.password = password
        self.id = id
        self.friend = friend

    def set_friends(self, password, *friends):
        if password == self.password:
            self.friend = friends
            return 'Operation complete successfully'
        else:
            return 'Invalid password'

    def info(self):
        if '\n' in self.name:
            return f"""Name: {self.name}Id: {self.id}Friend: {self.friend}"""
        else:
            return f"""Name: {self.name}\nId: {self.id}\nFriend: {self.friend}"""


root = Tk()
root.title('Person')
root.geometry('400x250')
root['bg'] = 'cyan'


def save():
    try:
        mlist = [f'{people.name}\n', f"{people.id}\n", f"{people.friend}"]
    except:
        mb.showerror('Error', 'At first you must create human!')
        return
    o = open('people.txt', 'w')
    o.writelines(mlist)
    o.close()


info = Text(root, width=40, height=7)
info.configure(state='disabled')
info.place(x=40, y=100)


def pin():
    global inputq
    root.withdraw()
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
        root.deiconify()

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
            num.configure(state='normal')
            num.delete(1.0, END)
            num.insert(INSERT, 'Successful')
            num.configure(state='disabled')
            moreq = Tk()
            moreq.resizable(width=False, height=False)
            moreq.title('More')
            moreq.geometry('400x250')
            moreq['bg'] = 'cyan'
            def check():
                checkq = Tk()
                checkq.resizable(width=False, height=False)
                checkq.title('Check')
                checkq.geometry('400x250')
                checkq['bg'] = 'cyan'
                try:
                    import Koteyka
                except:
                    koteykaQ = 'NO'
                else:
                    koteykaQ = 'OK'

                try:
                    import time
                except:
                    timeQ = 'NO'
                else:
                    timeQ = 'OK'

                try:
                    import random
                except:
                    randomQ = 'NO'
                else:
                    randomQ = 'OK'
                Label(checkq, bg='cyan', text='Тест модулей', font='Arial 15').place(x=10, y=10)
                Label(checkq, bg='cyan', font='Arial 12', text=f'Koteyka: {koteykaQ}').place(x=10, y=50)
                Label(checkq, bg='cyan', font='Arial 12', text=f'Time: {timeQ}').place(x=10, y=80)
                Label(checkq, bg='cyan', font='Arial 12', text=f'Random: {randomQ}').place(x=10, y=110)
            Button(moreq, command=check, text='Проверка', width=7, bg='lemon chiffon', activebackground='orange', height=3).place(x=10, y=10)

    Button(pinq, command=lambda: add(1), text='1', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=10, y=40)
    Button(pinq, command=lambda: add(2), text='2', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=70, y=40)
    Button(pinq, command=lambda: add(3), text='3', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=130, y=40)
    Button(pinq, command=lambda: add(4), text='4', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=10, y=105)
    Button(pinq, command=lambda: add(5), text='5', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=70, y=105)
    Button(pinq, command=lambda: add(6), text='6', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=130, y=105)
    Button(pinq, command=lambda: add(7), text='7', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=10, y=170)
    Button(pinq, command=lambda: add(8), text='8', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=70, y=170)
    Button(pinq, command=lambda: add(9), text='9', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=130, y=170)
    Button(pinq, command=lambda: add(0), text='0', width=5, bg='lemon chiffon', activebackground='orange', height=3).place(x=70, y=235)
    Button(pinq, command=clear, text='Reset', width=5, bg='light grey', activebackground='grey', height=3).place(x=10, y=235)
    Button(pinq, command=cancel, text='Cancel', width=5, bg='light grey', activebackground='grey', height=3).place(x=130, y=235)


def get_info():
    try:
        people.name
    except:
        mb.showerror('Error', 'At first you must create human!')
        return
    else:
        info.configure(state='normal')
        info.delete(1.0, END)
        info.insert(INSERT, people.info())
        info.configure(state='disabled')


def create():
    root.withdraw()
    cre = Tk()
    name = StringVar(cre)
    idq = StringVar(cre)
    friend = StringVar(cre)
    cre.title('Create')
    cre.geometry('400x250')
    cre['bg'] = 'cyan'

    Label(cre, text='Name:', bg='cyan').place(x=10, y=10)
    Entry(cre, textvariable=name, width=20).place(x=80, y=10)

    Label(cre, text='Id:', bg='cyan').place(x=10, y=40)
    Entry(cre, textvariable=idq, width=20).place(x=80, y=40)

    Label(cre, text='Friend:', bg='cyan').place(x=10, y=70)
    Entry(cre, textvariable=friend, width=20).place(x=80, y=70)

    def save():
        try:
            global people
            people = Person(name.get(), idq.get(), 1, friend.get())
            print('Operation complete successfully')
        except:
            print("Error while adding new human!")
        root.deiconify()
        cre.destroy()

    Button(cre, text='Save', command=save).place(x=80, y=140)

    cre.mainloop()


def load():
    global people
    o = open('people.txt', 'r')
    q = o.readlines()
    o.close()
    people = Person(q[0], q[1], 1, q[2])


Button(root, command=create, text='Create', bg='lemon chiffon').place(x=10, y=10)
Button(root, command=get_info, text='Info', bg='lemon chiffon').place(x=70, y=10)
Button(root, command=save, text='Save to file', bg='lemon chiffon').place(x=130, y=10)
Button(root, command=load, text='Load from file', bg='lemon chiffon').place(x=230, y=10)
Button(root, command=pin, text='More', bg='yellow').place(x=350, y=220)
root.resizable(width=False, height=False)

root.mainloop()
