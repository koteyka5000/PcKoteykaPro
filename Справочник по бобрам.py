from tkinter import *
import random
from threading import Thread
import time
from tkinter import messagebox as mb


def doHackR():
    doHack = random.randint(0, 1)
    if doHack == 1:
        doHack = True
    else:
        doHack = False
    return doHack


def animation(name, typeB):
    an = Tk()
    an.title(name)
    an["bg"] = "cyan"
    an.geometry("300x200")
    an.resizable(0, 0)
    Label(an, bg="cyan", text="Подключен сервер: ").grid(row=1)
    a1 = Label(an, bg="cyan", text="Скачанны данные: ")
    a1.grid(row=2)
    Label(an, bg="cyan", text="Данные расшифрованны: ").grid(row=3)
    a = Label(an, bg="cyan", text="Успешно: ")
    a.grid(row=4)

    def Start1():
        time.sleep(4)
        Label(an, bg="cyan", text="ДА").grid(row=1, column=6)
        time.sleep(2)
        a2 = Label(an, bg="cyan", text="ДА")
        a2.grid(row=2, column=6)
        time.sleep(3)
        Label(an, bg="cyan", text="ДА").grid(row=3, column=6)
        time.sleep(6)
        Label(an, bg="cyan", text="ДА").grid(row=4, column=6)
        a['text'] = "Инициализация..."
        time.sleep(1)
        if doHackR() or 1:
            an["bg"] = 'red'
            time.sleep(1)
            btn["bg"] = "lime"
            time.sleep(0.5)
            an["bg"] = "lime"
            time.sleep(2)
            an["bg"] = "red"
            time.sleep(0.3)
            a["bg"] = "yellow"
            time.sleep(0.3)
            a['fg'] = 'blue'
            time.sleep(0.3)
            btn['fg'] = 'gold'
            time.sleep(0.3)
            btn["text"] = '?№(;DR33$'
            a["text"] = "&Sdh(HAsd4@"
            time.sleep(0.3)
            a1["text"] = "Взл0№мА*н0"
            a1["font"] = "Arial 13"
            a2["font"] = "Arial 16"
            time.sleep(0.3)
            a2["text"] = "0\"Л;Ё*Г"
            for i in range(30):
                Label(root, bg="gold", text='Вз^л(0)Ма*№нНо!0').grid(row=i)
                time.sleep(0.2)
                for j in range(20):
                    Label(an, bg="gold", text='Вз^л(0)Ма*№нНо!0').grid(row=i, column=j)
                    Label(root, bg="gold", text='Вз^л(0)Ма*№нНо!0').grid(row=i, column=j)
            for i in range(400):
                root.geometry(f"{400 + i}x{200 + i}")
                root.update()

            olq = Tk()
            olq.geometry("400x300")
            olq.title("@^%dGASfh#*F^@")
            olq["bg"] = "pink"
            nameE = StringVar(olq)
            passE = StringVar(olq)
            Label(olq, text="Имя: ").grid(row=1, column=1)
            Label(olq, text="Пароль: ").grid(row=2, column=1)
            Entry(olq, textvariable=nameE, show='').grid(row=1, column=2)
            Entry(olq, textvariable=passE, show='').grid(row=2, column=2)

            def login():
                mb.showinfo('@#$%^&*', f"name={nameE.get()}, pass={passE.get()}")
                mb.showerror("Пересылаю доступ бобру...", "Пересылаю доступ бобру...              ")
                for j in range(20):
                    mb.showerror("@#4#", f"DA@W{j}D@^DS")

            Button(olq, text='Зарегистрироваться', command=login).grid(row=3)
            Button(root, text="   ").grid(row=2)

            olq.mainloop()
        else:
            pass

    btn = Button(an, command=lambda: Thread(target=Start1).start(), text="СТАРТ")
    btn.place(x=30, y=140)
    an.mainloop()


root = Tk()
root.title("Справочник по бобрам")
root["bg"] = "cyan"
root.geometry("400x200")

Button(root, text="Олег", command=lambda: animation("Бобёр Олег", 1), activebackground="gold", bg='gold').place(x=20,
                                                                                                                y=20)
Button(root, text="Семён", command=lambda: animation("Бобёр Семён", 2), activebackground="gold", bg='gold').place(x=100,
                                                                                                                  y=20)
Button(root, text="Василий", command=lambda: animation("Бобёр Василий", 3), activebackground="gold", bg='gold').place(
    x=180, y=20)

root.mainloop()
