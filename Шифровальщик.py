# Импортируем
from tkinter import *
from tkinter import messagebox as mb
dologO = open("doLog.txt", "r")
dologR = dologO.read()
dologO.close()

try:
    from cryptography.fernet import Fernet
except:
    mb.showerror("Ну вот, уже ошибка :(",
                 "Произошла ошибка модуля Fernet(Из cryptography), программа не может продолжить "
                 "работу, так как этот модуль необходим :(")
try:
    import pyperclip
except:
    mb.showerror("Ошибка", "Произошла ошибка модуля pyperclip, программа не может продолжить работать :(")


def Paste1():
    paste2 = pyperclip.paste()
    txt.insert(0, paste2)


try:
    open('doCopy.txt', "r")
except:
    a = open('doCopy.txt', "w")
    a.write("0")
    a.close()
try:
    a = open("Key.txt", "r")
except:
    a = open("Key.txt", "w")
    a.write("KoteykaSuperDuperSecuryPack0803825516377162=")

a = open("Key.txt", "r")
cipher_key = a.read()
a.close()


# Настройки
def settings():
    # Уничтожаем главное окно (с ним не работает)
    try:
        root.destroy()
    except:
        pass

    sett = Tk()
    sett.title("Настройки")
    sett.geometry('270x200')
    sett['bg'] = 'cyan'
    sett.resizable(width=False, height=False)
    doCopySet = IntVar()

    doCopyO = open("doCopy.txt", "r")
    doCopyR = doCopyO.read()
    doCopyO.close()
    doLogO = open("doLog.txt", "r")
    doLogR = doLogO.read()
    doLogO.close()

    qw = Checkbutton(sett, bg="cyan", text="Автоматическое копирование", variable=doCopySet, activebackground="#00fff2")
    if doCopyR == str(1):
        qw.select()
    qw.pack()

    logtxt = IntVar()
    qwe = Checkbutton(sett, bg="cyan", text="Откладка в log", variable=logtxt, activebackground="#00fff2")
    if doLogR == str(1):
        qwe.select()
    qwe.pack()


    def changeKey():
        CK = Tk()
        Key = StringVar(CK)
        CK.title("Изменить ключ")
        CK.geometry('300x180')
        CK['bg'] = 'cyan'
        CK.resizable(width=False, height=False)
        Entry(CK, textvariable=Key, width=44).pack()

        def FirstKey():
            def FirstKey1():
                keyO = open("Key.txt", "w")
                keyO.write("KoteykaSuperDuperSecuryPack0825489264871847=")
                keyO.close()
                mb.showinfo("Успешно", "Восстановлено значение по умолчанию №1")

            def FirstKey2():
                keyO = open("Key.txt", "w")
                keyO.write("KoteykaSuperDuperSecuryPack1234567890123456=")
                keyO.close()
                mb.showinfo("Успешно", "Восстановлено значение по умолчанию №2")

            def FirstKey3():
                keyO = open("Key.txt", "w")
                keyO.write("KoteykaSuperDuperSecuryPack0803825516377162=")
                keyO.close()
                mb.showinfo("Успешно", "Восстановлено значение по умолчанию №3")

            Fk = Tk()
            Fk.title("Выбор ключа")
            Fk.geometry('200x100')
            Fk['bg'] = 'cyan'
            Fk.resizable(width=False, height=False)
            Button(Fk, text="№1", command=FirstKey1, bg='lime', activebackground="#00fff2").place(x=20, y=10)
            Button(Fk, text="№2", command=FirstKey2, bg='lime', activebackground="#00fff2").place(x=80, y=10)
            Button(Fk, text="№3", command=FirstKey3, bg='lime', activebackground="#00fff2").place(x=140, y=10)

        def exampleKeys():
            mb.showinfo("Примеры кода", "KoteykaSuperDuperSecuryPack1234567890123456=\n\n"
                                        "Lolqwerty1234567890qweqweqweUIOPPLdQAZuYKeK=\n\n"
                                        "ThisIsTESTCodeLOLqwertyMYSuperDuperSecuryGG=\n\n"
                                        "UdAS8d668EA8SBGD80ABVSdiSVBdkafbvAFs3827rts=")

        def randomKey():
            cipher_key = Fernet.generate_key()

            a = mb.askyesnocancel("Вам подходит это ключ?:", cipher_key)
            while a != None:
                if a == True:
                    keyO = open("Key.txt", "w")
                    cipher_key = cipher_key.decode('utf-8')
                    keyO.write(cipher_key)
                    keyO.close()
                    mb.showinfo("Успешно", f"Новый код: {cipher_key}")
                    CK.destroy()
                    break
                elif not a:
                    cipher_key = Fernet.generate_key()
                    a = mb.askyesnocancel("Вам подходит это ключ?:", cipher_key)

        def saveKey():
            KeyQ = Key.get()
            if len(KeyQ) == 44:
                if KeyQ.find(" ") == -1:
                    if KeyQ.find("=") == 43:
                        if set("!\"\'!@#$%^&*№;%:?*()¤&").isdisjoint(KeyQ):
                            if set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ').isdisjoint(
                                    KeyQ):
                                keyO = open("Key.txt", "w")
                                keyO.write(KeyQ)
                                keyO.close()
                                mb.showinfo("Успешно", f"Новый код: {KeyQ}")
                                CK.destroy()
                            else:
                                mb.showerror("Ошибка кода:", "Нельзя использовать русские буквы")
                        else:
                            mb.showerror("Ошибка кода:", "Нельзя использовать спецсимволы")
                    else:
                        mb.showerror("Ошибка кода:", "Не обнаружено '=' в конце кода")
                else:
                    mb.showerror("Ошибка кода:", "Нельзя использовать пробелы")
            else:
                mb.showerror("Ошибка кода:", f"Длинна кода: {len(KeyQ)}, а ожидалось 44")

        try:
            Label(CK, text="Примечания: \n Код содержит 44 символа, включая \n"
                           "Обязательное \"=\" в конце", fg='blue', bg='cyan').pack()

            Button(CK, text="Сохранить и выйти", command=saveKey, bg='lime', activebackground="#00fff2").pack()
            Button(CK, text="Примеры кода", command=exampleKeys, bg='yellow', activebackground="#00fff2").place(x=200,
                                                                                                                y=150)
            Button(CK, text="Сгенерировать случайный ключ", command=randomKey, bg='lime',
                   activebackground="#00fff2").place(x=55, y=100)
            Button(CK, text="Выбрать код из основных", command=FirstKey, bg='lime', activebackground="#00fff2").place(
                x=2, y=150)
        except:
            pass

    # Сохраняем значение в файл
    def save():
        logO = open("doLog.txt", "w")
        doCopyO = open("doCopy.txt", "w")
        doCopyO.write(str(doCopySet.get()))
        doCopyO.close()

        if logtxt.get() == 1:
            if mb.askyesno("Информация", "Режим откладки в log включает откладку действий в файл log.txt, с помощью "
                                         "него можно просмотреть действия, которые выполнялись, и подробную информацию"
                                         " о ошибках, которые произошли во время работы "):
                logO.write(str(1))
            else:
                logO.write(str(0))

        msg = "Перезапустите приложение"
        logO.close()
        mb.showinfo("Информация", msg)
        quit()

    # Информация
    def devOpen():
        dev = Tk()
        dev.title("Информация о приложении")
        dev.geometry('350x200')
        dev['bg'] = 'cyan'
        dev.resizable(width=False, height=False)

        key = open("Key.txt", "r")
        keyR = key.read()
        key.close()

        def copyKey():
            pyperclip.copy(keyR)
            mb.showinfo("Скопировано!", "Успешно          ")

        Label(dev, text=f"Установленный код доступа:", fg='blue', bg='cyan').pack()
        Label(dev, text=keyR, fg='red', bg='lime', font='Arial 10').pack()
        Label(dev, text='Создатель: Koteyka5000', font='Arial 10', fg='blue', bg='cyan').place(x=130, y=150)
        Label(dev, text='Inst: @Koteyka5000', font='Arial 15', fg='gold', bg='cyan').place(x=160, y=170)

        Button(dev, text="Назад", command=dev.destroy, bg='yellow', activebackground="#00fff2").place(x=10, y=170)
        Button(dev, text='Скопировать!', bg='yellow', activebackground="#00fff2", command=copyKey).place(x=260, y=50)

        dev.mainloop()

    Button(sett, text="Сохранить и выйти", command=save, bg='lime', activebackground="#00fff2").place(x=140, y=170)
    Button(sett, text="Информация", command=devOpen, bg='yellow', activebackground="#00fff2").place(x=10, y=170)
    Button(sett, text="Изменить код доступа", command=changeKey, bg='cyan', activebackground="#00fff2").pack()

    sett.mainloop()


# Шифруем
def da():
    global textToCopy, text
    # Ключ
    try:
        cipher = Fernet(cipher_key)
        # Получаем значение из message.StringVar
        mes = message.get()
        mes = mes.encode()
        mesLock = cipher.encrypt(mes)
        textToCopy = mesLock
        # Текстовое поле для вывода
        text = Text(width=40, height=7)
        text.insert(INSERT, mesLock)
        mesLock = mesLock.decode('utf-8')



    except:
        text = Text(width=40, height=7)
        text.insert(INSERT, "Ой, ошибка ключа! Скорее всего, произошла какая-то ошибка записи. Жаль, что так произошло,"
                            " но я попробую исправить данную неполадку, Вы можете восстановить любой из 3 "
                            "основных кодов, или оставить свой")
        text.configure(state='disabled')
        text.place(x=40, y=100)
        mb.showinfo("Сообщите информацию)",
                    "Пожалуйста, сообщите ваш ключ, чтобы я мог понять, какой символ вызвал ошибку :)")

        if mb.askquestion("Средство восстановления", "Открыть настройки?                                  ") == "yes":
            settings()
    doCopyO = open("doCopy.txt", "r")
    doCopyR = doCopyO.read()

    if doCopyR == str(1):
        pyperclip.copy(str(mesLock))
    doCopyO.close()

    text.configure(state='disabled')
    text.place(x=40, y=100)
    txt.delete(0, END)


def unlock():
    # Расшифровываем
    global textToCopy
    # Ключ
    try:
        cipher = Fernet(cipher_key)
        # Получаем значение из message.StringVar
        mes = message.get()
        mes = mes.encode()
        textToCopy = mes
        # пробуем расшифровать
        decrypted_text = cipher.decrypt(mes)
        decrypted_text = decrypted_text.decode('utf-8')
        text = Text(width=40, height=7)
        text.insert(INSERT, decrypted_text)
        text.configure(state='disabled')
        text.place(x=40, y=100)
        doCopyO = open("doCopy.txt", "r")
        doCopyR = doCopyO.read()
        if doCopyR == str(1):
            pyperclip.copy(decrypted_text)
        doCopyO.close()

    # При ошибке
    except:
        text = Text(width=40, height=7)
        text.insert(INSERT, "Ошибка при обработке")
        text.configure(state='disabled')
        text.place(x=40, y=100)
    txt.delete(0, END)


def Copy():
    global textToCopy
    try:
        textToCopy = textToCopy.decode('utf-8')
    except AttributeError:
        pass
    pyperclip.copy(textToCopy)


textToCopy = ""
# Главное окно
root = Tk()
root.title("Шифовальщик")
root.geometry('400x250')
root['bg'] = 'cyan'

# valuesRoot.attributes('-fullscreen', True)
root.resizable(width=False, height=False)
message = StringVar()
# Текстовое поле
txt = Entry(textvariable=message)
txt.place(x=130, y=40)
# Надпись
lbl1 = Label(root, text="Введите сообщение:", fg='#2432d1', font="Arial 12", bg='cyan')
lbl1.place(x=120, y=10)
# Кнопки
message_button = Button(text="Зашифровать!", command=da, bg='lime', activebackground="#00fff2")
message_button.place(x=100, y=65)
btn1 = Button(text="Расшифровать!", command=unlock, bg='lime', activebackground="#00fff2")
btn1.place(x=200, y=65)
btn1 = Button(text="Выход", command=root.destroy, bg='grey', activebackground="grey22")
btn1.place(x=180, y=220)
Button(text="Вставить", command=Paste1, bg='lime', activebackground="#00fff2").place(x=270, y=35)
Button(text="Копировать", command=Copy, bg='lime', activebackground="#00fff2").place(x=279, y=5)
Button(text="Настройки", command=settings, bg="grey", activebackground="grey22").place(x=5, y=220)

# Назначаем родительским
root.mainloop()
