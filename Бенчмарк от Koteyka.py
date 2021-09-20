try:
    import time
    from tkinter import *
except:
    print("Ой! Ошибка импорта модулей, Программа может"
          "работать неправильно!! Интересно, как модуля"
          "Time Может не быть...")


qwe = False
print("Тестирование")
time.sleep(0.5)
print("ПК")
time.sleep(0.5)
print("от")
time.sleep(0.5)
print("Koteyka")
time.sleep(0.5)
print("""
Это не фейковая программа,
которая рандомно генерирует числа по 
производительности. Вы можете заметить, 
что при работе тестов загрузка процесса
'Python' возрастает. К сожалению,
у меня не получилось распределять 
задачи на потоки, чтобы это произошло быстрее,
и загрузка цп была больше. Еслии вы залезете
в код, то можете заметить, что модуть рандом
не импортируется, а значит ведутся настоящие 
вычисления.
""")

print("Продолжение через")
print('5', end=" ")
time.sleep(1)
print(4, end=" ")
time.sleep(1)
print('3', end=" ")
time.sleep(1)
print('2', end=" ")
time.sleep(1)
print('1')
time.sleep(1)
print("!!ТЕСТ НАЧНЁТСЯ АВТОМАТИЧЕСКИ!!")
print("!!Желательно закрыть все окна, чтобы результат был лучше!!")
time.sleep(1)
print("Начинаем через...")
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("""
#############################
##########СТАРТ##############
#############################

""")


class Test:

    def socr(num):
        q = "%.2f" % num
        return q

    def coolBal(self):
        q = len(str(self))
        q = int(q)
        q -= 3
        doPrintZero = True
        if q == 2 or q == 1:
            q = 1000
        elif q == 3 and a < 200:
            q = 200
        elif q == 3 and a < 300:
            q = 300
        elif q == 3 and a < 400:
            q = 400
        elif q == 3 and a < 500:
            q = 500
        else:
            doPrintZero = False
            return 0

        if doPrintZero:
            q = float(q)
            # q = int(q)
            self = float(self)
            # self = int(self)
            if q - self < 0:
                return 0
            else:
                return q - self


q = 0
# a = int(input("Sd: "))
a = 3
if a == 3:
    q1 = time.time()
    print("0%")
    for i in range(0):
        qwe1 = time.time()
        if qwe == False:
            qw1 = time.time()
        gruz = 99999 ** 99999
        gruz1 = 99999 ** 999999
        gruz2 = 9999 ** 99999
        gruz3 = gruz + gruz1 + gruz2
        # print("================================")
        if not qwe:
            qw2 = time.time()
            qwe = True
        q += 1
        qwe2 = time.time()
        print(f"\rТест под номером {q} прошёл успешно, и занял {Test.socr(qwe2 - qwe1)} секунд",end='')
    print('\n')
    q2 = time.time()
    q3 = Test.socr(q2 - q1)
    FirstTest = Test.coolBal(q3)
    print("----------------------------------------")
    print(f"ПК набрал баллов в 1 тесте: {FirstTest}")
    print("----------------------------------------")
    print('Начинаем 2 тест')
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("""
#############################
##########СТАРТ##############
#############################
""")
qwe1 = time.time()
for i in range(40000):
    gruz = 99 ** 9999
    print(f"\rИдет тест под номером {i} / 40000", end='')
print('\n')
qwe2 = time.time()

q4 = Test.socr(qwe2 - qwe1)
SecondTest = Test.coolBal(q4)

print(f"ПК набрал баллов во 2 тесте: {SecondTest}")

print("Начинаем 3 тест")
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("""
#############################
##########СТАРТ##############
#############################
""")
qw1 = time.time()
for i in range(1001):
    gruz = 9999 ** 9999
    gruz1 = (len(str(gruz)))
    print(f"\rИдёт тест под номером {i} из 1000", end='')

qw2 = time.time()
ThreeTest = Test.socr(qw2 - qw1)
ThreeTest = Test.coolBal(ThreeTest)
print("""ВНИМАНИЕ: СЛЕДУЮЩИЙ ТЕСТ
ДЛЯ ДОВОЛЬНО МОЩНЫХ ПК,
ОН ВЫПОЛНЯЕТСЯ 5.000.000 РАЗ!!
ЕСЛИ ВЫ ХОТИТЕ ПОПРОБОВАТЬ
ЭТОТ ТЕСТ, ТО ВВЕДИТЕ 
Да
ЕСЛИ НЕТ, ТО НАЖМИТЕ Enter""")


doHardTest = input("Да/Enter")
if doHardTest == 'Да' or doHardTest == "да":
    doMiddleFour = True
    qw1 = time.time()
    for i in range(5000001):
        gruz = 10 ** 10
        print(f"\rИдёт тест 4 под номером {i} из 5.000.000", end='')
    print('\n')
    qw2 = time.time()
    FourTest = Test.socr(qw2 - qw1)
    FourTest = Test.coolBal(FourTest)
else:
    print("!!Тест отменён!!")
    FourTest = "Не проводился"
    doMiddleFour = False
if doMiddleFour:
    middle = (float(FirstTest) + float(SecondTest) + float(ThreeTest) + float(FourTest)) / 4
else:
    middle = (float(FirstTest) + float(SecondTest) + float(ThreeTest)) / 3
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("РЕЗУЛЬТАТЫ")
print(f"Первый тест: {FirstTest}")
print(f"Второй тест: {SecondTest}")
print(f"Третий тест: {ThreeTest}")
print(f"Четвёртый тест: {FourTest}")
print(f"Средняя оценка ПК: {Test.socr(middle)}")
print("")
print("Полелись результатами в группу :)")
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
