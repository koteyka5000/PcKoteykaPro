# Импортируем
from tkinter import *
from tkinter import messagebox as mb
import datetime
import os
import time
from threading import Thread
import pyautogui

dologO = open("doLog.txt", "r+")
dologR = dologO.read()
try:
    dologR = int(dologR)
except:
    dologR = 0
dologO.close()


def log(text, doExit=0):
    if dologR:
        logO = open("log.txt", 'a', encoding="UTF-8")
        now = datetime.datetime.now()
        time = now.strftime("%d.%m.%Y %H:%M:%S")
        txtW = f"[{time}]: {text}\n"
        logO.write(txtW)
        logO.close()
    if doExit == 1:
        exit()
    if doExit == 2:
        if mb.askyesno("Вы уверены?", "Некоторая информация не сохранится"):
            exit()


log("\n\n Запущено окно")

try:
    from cryptography.fernet import Fernet
except:
    mb.showerror("Ну вот, уже ошибка :(",
                 "Произошла ошибка модуля Fernet(Из cryptography), программа не может продолжить "
                 "работу, так как этот модуль необходим :(")
    log("!Ошибка! Ошибка импорта модуля Fernet")
    exit()

log("Модуль Fernet успешно импортирован")

try:
    import pyperclip
except:
    mb.showerror("Ошибка", "Произошла ошибка модуля pyperclip, программа не может продолжить работать :(")
    log("!Ошибка! Ошибка импорта модуля pyperclip")
    exit()
log("Модуль Pyperclip успешно импортирован")


def Paste1():
    paste2 = pyperclip.paste()
    log(f"Вставлен текст {paste2}")
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


    sett = Tk()
    sett.title("Настройки")
    sett.geometry('270x250')
    sett['bg'] = 'cyan'
    sett.resizable(width=False, height=False)
    doCopySet = IntVar(sett)
    sett.protocol("WM_DELETE_WINDOW", lambda: log("Окно закрывается", 2))
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

    logtxt = IntVar(sett)
    qwe = Checkbutton(sett, bg="cyan", text="Откладка в log", variable=logtxt, activebackground="#00fff2")
    if doLogR == str(1):
        qwe.select()
    qwe.pack()

    def changeKey():
        log("Открыто окно изменения ключа")
        CK = Tk()
        Key = StringVar(CK)
        CK.title("Изменить ключ")
        CK.geometry('300x180')
        CK['bg'] = 'cyan'
        CK.resizable(width=False, height=False)
        Entry(CK, textvariable=Key, width=44).pack()

        def FirstKey():
            log("Открыто окно выбора ключа из основных")

            def FirstKey1():
                keyO = open("Key.txt", "w")
                keyO.write("KoteykaSuperDuperSecuryPack0825489264871847=")
                keyO.close()
                mb.showinfo("Успешно", "Восстановлено значение по умолчанию №1")
                log("Восстановлен ключ номер 1")

            def FirstKey2():
                keyO = open("Key.txt", "w")
                keyO.write("KoteykaSuperDuperSecuryPack1234567890123456=")
                keyO.close()
                mb.showinfo("Успешно", "Восстановлено значение по умолчанию №2")
                log("Восстановлен ключ номер 2")

            def FirstKey3():
                keyO = open("Key.txt", "w")
                keyO.write("KoteykaSuperDuperSecuryPack0803825516377162=")
                keyO.close()
                mb.showinfo("Успешно", "Восстановлено значение по умолчанию №3")
                log("Восстановлен ключ номер 3")

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
            log("Открыто окно выбора случайного ключа")
            a = mb.askyesnocancel("Вам подходит это ключ?:", cipher_key)
            while a != None:
                if a == True:
                    keyO = open("Key.txt", "w")
                    cipher_key = cipher_key.decode('utf-8')
                    keyO.write(cipher_key)
                    keyO.close()
                    mb.showinfo("Успешно", f"Новый код: {cipher_key}")
                    log(f"Установлен новый код: {cipher_key}")
                    CK.destroy()
                    break
                elif not a:
                    cipher_key = Fernet.generate_key()
                    a = mb.askyesnocancel("Вам подходит это ключ?:", cipher_key)

        def saveKey():
            log("Попытка сохранения ключа")
            KeyQ = Key.get()
            if len(KeyQ) == 44:
                if KeyQ.find(" ") == -1:
                    if KeyQ.find("=") == 43:
                        if set("!\"\'!@#$%^&*№-_;%:?*()¤&").isdisjoint(KeyQ):
                            if set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ').isdisjoint(
                                    KeyQ):
                                keyO = open("Key.txt", "w")
                                keyO.write(KeyQ)
                                keyO.close()
                                mb.showinfo("Успешно", f"Новый код: {KeyQ}")
                                log(f"Установлен новый код: {KeyQ}")
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
        log('Сохраненяются настройки')
        logO = open("doLog.txt", "w")
        doCopyO = open("doCopy.txt", "w")
        doCopyO.write(str(doCopySet.get()))
        doCopyO.close()

        if logtxt.get() == 1:
            mb.showinfo("Информация", "Режим откладки в log включает откладку действий в файл log.txt, с помощью него "
                                      "можно просмотреть действия, которые выполнялись, и подробную информацию"
                                      " об ошибках, которые произошли во время работы ")
            logO.write(str(1))

        else:
            log("Отключён режим откладки")
            logO.write(str(0))
        logO.close()
        mb.showinfo("Успешно", "Настройки сохранены")
        sett.destroy()

    # Информация
    def devOpen():
        log("Открыто окно информации")
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
            log(f"Скопирован текущий ключ ({keyR})")
            mb.showinfo("Скопировано!", "Успешно          ")

        Label(dev, text=f"Установленный код доступа:", fg='blue', bg='cyan').pack()
        Label(dev, text=keyR, fg='red', bg='lime', font='Arial 10').pack()
        Label(dev, text='Создатель: Koteyka5000', font='Arial 10', fg='blue', bg='cyan').place(x=130, y=150)
        Label(dev, text='Inst: @Koteyka5000', font='Arial 15', fg='gold', bg='cyan').place(x=160, y=170)

        Button(dev, text="Назад", command=dev.destroy, bg='yellow', activebackground="#00fff2").place(x=10, y=170)
        Button(dev, text='Скопировать!', bg='yellow', activebackground="#00fff2", command=copyKey).place(x=260, y=50)

        dev.mainloop()

    def ClearLog():
        if mb.askyesno("Вы уверены?", "В файле log могут содержаться отчёты об ошибках, они будут безврозратно "
                                      "удалены, продолжить?"):
            logO = open("log.txt", 'w', encoding="UTF-8")
            logO.write("")
            logO.close()

    def devCmd():
        if mb.askyesno("CMD", "В консоле сняты все защиты, можно устанавливать любые ключи, или, например изменять "
                              "значения файлов напрямую. Запустить консоль?"):
            mb.showinfo("Информация", "Консоль работает через консоль интепритатора (Не в окне)")
            print("!!!! ПОСЛЕ ЗАВЕРШЕНИЯ НАПИШИТЕ КОМАНДУ exit !!!!")
            log("Запущена Консоль Разработчика")
            command = ''
            while command != "exit":
                def ChangeKeyCMD():
                    log("(CMD) Запущен режим принудительного изменения ключа")
                    keyCMD = input("Введите ключ: ")
                    keyO = open("Key.txt", "w")
                    keyO.write(keyCMD)
                    print(f"Успешно Новый ключ: {keyCMD}")
                    log(f"(CMD) Установлен новый ключ: {keyCMD}")

                def ChangeFile():
                    log("(CMD) Запущен режим принудительного изменения файлов")
                    print("Файлы:\n1) doLog.txt\n2) doCopy.txt")
                    keyCMD = input("Введите номер файла: ")
                    if keyCMD == "1":
                        q = open("doLog.txt", 'r')
                        print(f"Значение сейчас: {q.read()}")
                        q.close()
                        q = open("doLog.txt", 'w')
                        CMDkey = input("Введите значение: ")
                        q.write(CMDkey)
                        print("Успешно")
                        log(f"(CMD) Для файла doLog.txt установлено значение {CMDkey}")
                        q.close()

                command = input("Команда: ")
                log(f"(CMD) Введена команда: {command}")
                functions = {'key': ChangeKeyCMD, 'files': ChangeFile, 'log': lambda: os.system("start " + "log.txt")}
                try:
                    functions[command]()
                except:
                    if command != "exit":
                        log(f"(CMD) Команда {command} вызвала ошибку")
                        print("Команда не найдена")
                    else:
                        print("Консоль остановлена")
                        log("Консоль остановленна")

    Button(sett, text="Сохранить и выйти", command=save, bg='lime', activebackground="#00fff2").place(x=140, y=220)
    Button(sett, text="Информация", command=devOpen, bg='yellow', activebackground="#00fff2").place(x=10, y=220)
    Button(sett, text="Изменить код доступа", command=changeKey, bg='cyan', activebackground="#00fff2").pack()
    Button(sett, text="Очистить log файл", command=ClearLog, bg='lime', activebackground="#00fff2").place(x=78, y=110)
    Button(sett, text="Открыть log файл", command=lambda: os.system("start " + "log.txt")).place(x=80, y=140)
    Button(sett, text="Консоль разработчика", command=devCmd, bg='lime', activebackground="#00fff2").place(x=66, y=80)

    sett.mainloop()


# Шифруем
def da():
    global textToCopy, text
    # Ключ
    try:
        cipher = Fernet(cipher_key)
        # Получаем значение из message.StringVar
        mes = message.get()
        log(f"Зашифровано сообщение {mes}")
        mes = mes.encode()
        mesLock = cipher.encrypt(mes)
        textToCopy = mesLock
        # Текстовое поле для вывода
        text = Text(width=40, height=7)
        text.insert(INSERT, mesLock)
        mesLock = mesLock.decode('utf-8')




    except:
        mes = message.get()
        log(f"!ОШИБКА!\nОшибка зашифровки сообщения \n{mes}\nключём \n{cipher_key}")
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
        log(f"Автоматически скопировано {mesLock}")
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
        log(f"Успешно расшифрованно сообщение {decrypted_text}")
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
        log(f"Ошибка расшифровки сообщения {decrypted_text}")
        text = Text(width=40, height=7)
        text.insert(INSERT, "Ошибка при обработке")
        text.configure(state='disabled')
        text.place(x=40, y=100)
    txt.delete(0, END)


def Copy():
    global textToCopy
    try:
        textToCopy = textToCopy.decode('utf-8')
        log(f"Скопировано {textToCopy}")
    except AttributeError:
        pass
    pyperclip.copy(textToCopy)


textToCopy = ""
# Главное окно
root = Tk()
root.title("Шифовальщик")
root.geometry('400x250')
root['bg'] = 'cyan'
root.protocol("WM_DELETE_WINDOW", lambda: log("Окно закрывается", 1))
root.withdraw()

if len(cipher_key) != 44:
    def func():
        time.sleep(0.5)
        pyautogui.press('enter')


    Thread(target=func).start()
    mb._show("Автозащита", "Проверка ключа...")
    mb.showwarning("Автозащита", "Кажется, длинна кода не 44 символа. Если это сделано ради эксперемента, то "
                                 "можете проигнорировать данное сообщение, но программа работать не будет. "
                                 "Если это произошло случайно, то можно восстановить код из основных "
                                 "или установить новый")
    log("Сработала автозащита по поводу ключа")

root.deiconify()

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
log("Окно проинициализировалось")
root.mainloop()
