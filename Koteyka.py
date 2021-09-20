import datetime
from multiprocessing import Process
import os
from tkinter import messagebox as mb
from tkinter import *
import random
import time
from cryptography.fernet import Fernet
import pickle

cipher_key = b"KoteykaSuperDuperSecuryPack1234567890123456="
cipher = Fernet(cipher_key)


def write_dict(dictionary, file):
    with open(file, 'wb') as out:
        pickle.dump(dictionary, out)


def read_dict(file):
    with open(file, 'rb') as inp:
        d_in = pickle.load(inp)
    return d_in


def doFileAlive(File, IfFalse=None, IfTrue=None):
    """
    Функция, которая проверяет наличие файла,
    и при желании в определённых случаях
    может туда что-либо записать

    :param File: Файл для проверки (расширение тоже указывать если есть)
    :param IfFalse: Что записать в файл если его нет, пропустите если не нужно изменять файл (создатся файл с именем
    файла которого указывали в проверки)
    :param IfTrue: Что записать в файл если он есть, пропустите если не нужно изменять файл
    :return True если файл есть или False если файла нет
    """
    try:
        open(File, "r")
    except FileNotFoundError:
        if IfFalse is not None:
            open(File, "w").write(IfFalse)
        return False
    else:
        if IfTrue is not None:
            open(File, 'w').write(IfTrue)
        return True


def pin(n):
    global inputq
    pinq = Tk()
    pinq.title('Enter pin')
    pinq.geometry('190x270')
    pinq['bg'] = 'cyan'
    pinw = str(n)
    inputq = ''

    def qqww(): print(inputq)

    def clear():
        global inputq
        inputq = ''

    def add(n):
        global inputq
        inputq += str(n)
        if inputq == pinw:
            print('YES')

    Button(pinq, command=qqww, text='More', bg='yellow').place(x=350, y=220)
    Button(pinq, command=lambda: add(1), text='1', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=10)
    Button(pinq, command=lambda: add(2), text='2', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=10)
    Button(pinq, command=lambda: add(3), text='3', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=10)
    Button(pinq, command=lambda: add(4), text='4', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=75)
    Button(pinq, command=lambda: add(5), text='5', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=75)
    Button(pinq, command=lambda: add(6), text='6', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=75)
    Button(pinq, command=lambda: add(7), text='7', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=140)
    Button(pinq, command=lambda: add(8), text='8', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=140)
    Button(pinq, command=lambda: add(9), text='9', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=140)
    Button(pinq, command=lambda: add(0), text='0', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=205)
    Button(pinq, command=lambda: clear(), text='Reset', width=5, bg='light grey', activebackground='grey',
           height=3).place(x=10, y=205)

def log(text, MoreActions=0):
    """
    Функция, которая записывает текст как log (С указанием времени и удобной записью)

    :param text: Текст который будет вставлен в log
    :param MoreActions: Дополнительные действия, которые можно использовать для удобства написания
    """

    logO = open("log.log", 'a', encoding="UTF-8")
    now = datetime.datetime.now()  # Получаем время
    timeQ = now.strftime("%d.%m.%Y %H:%M:%S")  # Преобразуем в удобный формат
    txtW = f"[{timeQ}]: {text}\n"
    logO.write(txtW)  # Записываем
    logO.close()  # Закрываем

    if MoreActions == 1:
        log("Приложение закрыто")
        exit(78)
    elif MoreActions == 2:
        if mb.askyesno("Вы уверены?", "Некоторая информация не сохранится"):
            exit(78)
    elif MoreActions == 3:
        exit(78)
    elif MoreActions == 4:
        logO = open("log.log", 'w', encoding="UTF-8")
        logO.write('')  # Очищает файл
        logO.close()
    elif MoreActions == 5:
        os.remove("log.log")  # Удалить файл


def DNSPLS(t):  # Не запускайте!
    timer = t / 100
    for i in range(101):
        print(f"{i}%", end='')
        time.sleep(timer)
        print("\r", end='')


def load(t2, process=False):  # Симулятор загрузки
    timer = t2 / 100  # Вычисляем, сколько времени нужно для полной загрузки
    if process:
        Process(target=DNSPLS, args=(t2,)).start()
    else:
        for i in range(101):
            print(f"{i}%", end='')
            time.sleep(timer)
            print("\r", end='')


class encryption_files:
    @staticmethod
    def lockFile(text, method=1, file=None, doWrite=False, doReturn=True, enrange=1):
        """
        Функция, которая зашифровывает текст


        :param method: Метод шифровки
        :param file: Файл, в которыйй будет записан зашифрованный текст
        :param text: Текст для зашифровки
        :param doWrite: Записывать ли в файл зашифрованный текст
        :param doReturn: Возвращать ли зашифрованный текст
        :param enrange: Шаг изменения букв (Лучше не менять или менять не сильно)
        :return: Зашифрованный текст
        """
        if not doWrite and not doReturn:
            pass
        else:
            if method == 1:
                text1 = str(text)
                text1 = text1.encode()
                encrypted_text = cipher.encrypt(text1)
                if doWrite:
                    testsO = open(file, 'wb')
                    testsO.write(encrypted_text)
                    testsO.close()
                if doReturn:
                    return encrypted_text.decode('utf-8')

            elif method == 2:  # Мой метод, не используйте для безопасного шифрования
                alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                alphaList = list(alpha)
                out = ''
                if set("!\"\'!@#$%^&*№-_;%:?*()¤&").isdisjoint(text):
                    for i in text:
                        out += alphaList[alpha.find(i) + enrange]
                    if doWrite:
                        testsO = open(file, 'w')
                        testsO.write(out)
                        testsO.close()
                    if doReturn:
                        return out
                else:
                    return "Текст не должен содержать специальных символов"

    @staticmethod
    def unlock_file(text=None, method=1, file=None, doWrite=False, doReturn=True, fileToWrite=None, enrange=1):
        """
        Функция, которая расшифровывает зашифрованный текст

        :param method: Метод расшифровки (должен совпадать с методом расшифровки)
        :param text: Текст для расшифровки
        :param file: Файл, в который был записан зашифрованный текст
        :param doReturn: Возвращать ли зашифрованный текст
        :param doWrite: Записывать ли в файл расшифрованный текст
        :param fileToWrite: В какой файл записывать расшифрованный текст. По умолчанию в тот, где был зашифрованный
        :param enrange: Шаг изменения букв (Лучше не менять или менять не сильно)
        :return: Расшифрованный текст
        """
        if text is None and file is None:
            return None
        if not doWrite and not doReturn:
            pass
        else:
            if fileToWrite is not None:
                doWrite = True
            if file is not None:
                testO = open(file, "rb")
                testR = testO.read()
                testO.close()

            else:
                testR = text.encode()

            if method == 1:
                try:
                    decrypted_text = cipher.decrypt(testR)
                except:
                    return 'Ошибка: неверный текст'
                decrypted_text = decrypted_text.decode('utf-8')
                if doWrite:
                    if fileToWrite is None:
                        open(file).write(decrypted_text)
                    else:
                        open(fileToWrite, "w").write(decrypted_text)
                if doReturn:
                    return decrypted_text

            elif method == 2:
                alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                alphaList = list(alpha)
                out = ''
                if text is not None:
                    for i in text:
                        out += alphaList[alpha.find(i) - enrange]

                elif file is not None:
                    testO = open(file, "r")
                    text = testO.read()
                    testO.close()
                    for i in text:
                        out += alphaList[alpha.find(i) - enrange]

                if doWrite:
                    if fileToWrite is None:
                        open(file).write(out)
                    else:
                        open(fileToWrite, "w").write(out)

                return out


def random_bool(T=1, F=1, method=1):
    """
    Функция, которая возвращает True или False.
    Также можно увеличить шанс выпадания определённого случая

    Без указания аргументов будет выпадать случайное значение с шансом 50/50

    :param method: Метод генерации
    :param T: Увеличение шанса на True
    :param F: Увеличение шанса на False
    :return: True или False
    """
    if T == 1 and F == 1:
        a = random.randint(0, 1)
        return bool(a)
    else:
        if method == 1:
            TrueS = []
            FalseS = []
            TrueE = 0
            FalseE = 0

            for i in range(T):
                a = random.randint(0, 1)
                TrueS.append(a)
            for j in range(F):
                a = random.randint(0, 1)
                FalseS.append(a)
            for a in TrueS:
                if a == 1:
                    TrueE += 1
            for a in FalseS:
                if a == 1:
                    FalseE += 1
            if FalseE < TrueE:
                return True
            elif TrueE < FalseE:
                return False
            else:  # Last update
                if F < T:
                    return True
                else:
                    return False
        elif method == 2:
            t = random.randint(0, T)
            f = random.randint(0, F)
            if t == f:
                if T > F:
                    return True
                elif F < T:
                    return False
                else:
                    a = random.randint(0, 1)
                    if a == 0:
                        return False
                    else:
                        return True
            elif t == T:
                return True
            elif f == F:
                return False
            else:
                return True


def cmd(key, command):
    if str(key) == encryption_files.unlock_file("gAAAAABgbe5tGDsyVx-jUofDnd-XGg1J7SJNMPaodgbiZaD4ERAXvXSCsCnSa8vG-UHC6K\
    uqaJgqREqQnYtKrg0WKhGvjZaclA=="):
        if type(command) == 'list':
            for a in command:
                os.system(a)
        elif type(command) == 'str':
            os.system(command)
    else:
        return "В целях безопасности вам нужно ввести верный защитный код"


class randomList:
    """
    Класс, функции в котором возвращают случайный список нужных значений
    """

    @staticmethod
    def numbers(a=None, b=None, returns=1, showErrors=True):
        """
        Функция, который возвращает случайный список цифр из нужного диапозона

        :param showErrors: Возвращать ли имя ошибки, принимает True или False
        :param returns: сколько элементов возвращать

        диапазон
        :param a: c какого числа
        :param b: до какого числа

        :return: Список элементов
        """

        if not showErrors:
            try:
                lists = []
                for i in range(returns):
                    listr = random.randint(a, b)
                    lists.append(listr)
                return lists
            except:
                pass
        else:
            if a is not None and b is not None:
                if isinstance(a, int):
                    if isinstance(b, int):
                        if b > a:
                            lists = []
                            for i in range(returns):
                                listr = random.randint(a, b)
                                lists.append(listr)
                            return lists
                        else:
                            return "Первое число должно быть меньше второго"
                    else:
                        return "переменная b не число"
                else:
                    return "переменная a не число"
            else:
                return "Не введены числа"

    """
    Для всех функций ниже:
    
    :param returns: Сколько элементов возвращать
    :return: Список элементов
    """

    @staticmethod
    def capitalLetters(returns=1):
        """
        Список заглавных букв
        """
        lists = []
        for i in range(returns):
            lists.append(random.choice(list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")))
        return lists

    @staticmethod
    def lowercaseLetters(returns=1):
        """
        Список строчных букв
        """
        lists = []
        for i in range(returns):
            lists.append(random.choice(list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")))
        return lists

    @staticmethod
    def letters(returns=1):
        """
        Список всех букв
        """
        lists = []
        for i in range(returns):
            lists.append(random.choice(list("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")))
        return lists


def letters(text, t=0.3):
    text = list(text)
    for i in range(len(text)):
        print(text[i], end='')
        time.sleep(t)


if __name__ == '__main__':
    letters("Koteyka", 0.3)
    print("""
    Информация:
    Пакет дополнений Koteyka
    Версия: 1.7.8
    Создатель: Koteyka
    Inst: @koteyka5000
    
    """)
    input("Нажмите Enter для продолжения -->")
    print("""
    Установка:
    1) Положить файл в папку с вашим файлом, 
    в котором Вы хотите использовать 
    модуль Koteyka.
    2) В начале кода написать:
    
    import Koteyka
    
    Использование:
    Для вызова функции из модуля напишите:
    Koteyka.<Имя функции или класса>
    Пример:
    print(Koteyka.randomList.numbers(0, 1, 10))
    Вывод:
    
    """)
    print(randomList.numbers(0, 1, 10))
    print("""
    P.S. Вывод может быть другим, тк
    это случайные числа
    """)
