import time
import random

chatExit = False
PromocodeR = 777
# act1
# act2
# act3
# act4
# act4IN
stoneLikeR = 0

print('#######################')
time.sleep(0.5)
print('#     КАМЕНЬ         #')
time.sleep(0.5)
print('#    ВЫ - КАМЕНЬ      #')
time.sleep(0.5)
print('#    От Koteyka       #')
time.sleep(0.5)
print('#######################')

time.sleep(1)
while (1):
    print("======================")
    print("Что вы хотите сделать?")
    print("Варианты ответа:")
    print("Подышать - 1")
    print("Подумать - 2")
    print("Запостить текст - 3")
    print("Осмотреться - 4")
    print("Поспать - 5")
    print("Играть в казино - 6")
    print("Зайти в чат - 7")
    print("Настройки - 8")
    act1 = input("Ведите число: ")
    if (act1 == str(1)):
        print("======================")
        print("Жаль, но вы просто камень, и не умеете дышать :(")
        print("======================")
        time.sleep(2)
    if act1 == str(2):
        print("======================")
        print("О чём будем думать?")
        print("Для выхода введите 0")
        print("Незнаю - 1")
        print("О жизни других камней - 2")
        print("======================")
        act2 = input("Введите число: ")
        if act2 == str(1):
            print("Ну вот и камень незнает")
            time.sleep(2)
        if (act2 == str(2)):
            print("""
#
Камень думает, что у всех камней очень интересная жизнь,
даже незная, какая жизнь может быть
у камней, почти таких же, как и он
#""")
            a = input("Нажмите Enter для продолжения")
    if (act1 == str(3)):
        print('=======')
        print("Введите сообщение:")
        a = input()
        print("Подождите, идёт отправка сообщения...")
        peopleLike = random.randint(2, 40)
        time.sleep(3)
        print('=======')
        print("Ваше сообщение понравилось", peopleLike, "камням")
        stoneLike = open("stoneLike.txt", "r")
        q1 = stoneLike.read()
        stoneLike.close()

        peopleLikeAll = int(q1) + peopleLike

        print("Общее количество лайков:", peopleLikeAll)
        print('=======')
        stoneLike = open("stoneLike.txt", "w")
        stoneLike.write(str(peopleLikeAll))
        stoneLike.close()
        time.sleep(4)
    if (act1 == str(4)):
        print("""
==================
Вокруг вы видете немного других
камней, которые наверное тоже
думают что им поделать,
также тут есть небольшое озеро,
зелёная твава, которая шатается
на ветру, и птиц, которые сидят на дереве
и поют песни
==================""")
        input("Нажмите Enter для продолжения")
    if (act1 == str(5)):
        print("=================")
        print("Вы попытались уснуть, но у вас не вышло")
        print("Попробовать поспать ещё - 1")
        print("Ну и ладно, не буду спать - 2")
        act3 = int(input("Введите число: "))
        if (act3 == 1):
            print("""
=================
Вы уснули, непонимая, сколько вы спали
вы просыпаетесь, и видите, что птицы улетели с дерева,
а мелкие камни немного сдвинулись от ветра
=================
""")
            time.sleep(7)
    if (act1 == str(6)):
        print("KAZINO")
        kazGame = int(input("Сколько раз играем?: "))
        for kazGameCount in range(0, kazGame, 1):
            kaz1 = random.randint(1, 4)
            kaz2 = random.randint(1, 4)
            kaz3 = random.randint(1, 4)
            print("=====================")
            print("Вам выпадают числа...")
            time.sleep(1)
            print(kaz1, end=" ")
            time.sleep(1)
            print(kaz2, end=" ")
            time.sleep(1)
            print(kaz3)
            if (kaz1 == kaz2 == kaz3):
                print("""Невероятная удача!!
        камень выйграл джекпот
        и теперь он  богат!!""")
            elif (kaz1 == kaz2 or kaz2 == kaz3):
                print("Камень победил!")
            else:
                print("Камень проиграл")

    if (act1 == str(7)):
        print("Внимание! Для выхода из чата введите 'выйти' ")
        time.sleep(3)
        chatNamePlayer = input("Введите ник: ")
        while (chatExit == False):
            CN = ["Камень:", "Аноним:", "Игрок:", "Кот:", "Стив:", "Человек:", "Ник:", "Герда:", "Джесси:"]
            CM = ["Всем привет", "NsjfСПАААМb72634", "Шо тут надо делать?)", "ЫЫЫЫ",
                  "Я камень :)", "Народ что тут надо делать",
                  "Блин у меня 2 по матеше и по физике(((",
                  "АААААААААААААААААААА", "123", "А у меня новый комп))))",
                  "Это моя любимая игра!!!", "Как вы оцените эиу игру?",
                  "Кот не может - ШАМПУНЬ ПОМОЖЕТ!", "У МЕНЯ КОТ НАСРАЛ♥",
                  "А как вашего кота зовут? Моего Шампунь", "Блин народ есть отвёртка?",
                  "Я уже год играю, не надоело! :)", "А куда вводить промокоды?",
                  "А вы хотите спать?", "Памагите меня затянуло, играю уже 4 часа!",
                  "Мне очень понравились промокоды и новые меню!!",
                  "Cпасибо разработчику за эту замечательную игру!!♥ ♥ ♥", "А вы успели забрать 200 лайков по "
                                                                           "промокоду KoteykaTOP? "


                  ]

            CNR = random.randint(0, len(CN) - 1)
            TimeR = random.randint(1, 3)
            CMR = random.randint(0, len(CM) - 1)
            mesR = random.randint(0, 1)
            print(CN[CNR], CM[CMR])
            time.sleep(1)
            if (mesR == 1):
                mes = input("Введите сообщение: ")
                if (mes == "выйти"):
                    break
                if (mes != "выйти"):
                    print(chatNamePlayer + ":", mes)
            time.sleep(TimeR)
            ##############
    if act1 == str(8):
        print("================")
        print("Очистить общее кол-во лайков - 1")
        print("Ввести промокод - 2")
        print("Консоль разработчика - 3")
        act4 = (input())
        if act4 == str(1):
            print("#########################################")
            print("##           Вы уверены?               ##")
            print("##     Вы НЕ сможете вернуть лайки!    ##")
            print("##         132 = ДА, 1 - НЕТ           ##")
            print("#########################################")
            act4IN = input("ОТВЕТ:           ")
            if (act4IN == str(132)):
                stoneLike = open("stoneLike.txt", "w")
                stoneLike.write(str(0))
                stoneLike.close()
                print("Успешно")
            else:
                print("""""")
                time.sleep(2)
        if (act4 == str(2)):
            print("Введите промокод:")
            Promocode = open("Promocode.txt", "r")
            PromocodeR = Promocode.read()
            Promocode.close()
            promocodesOPEN = open("Promocodes.txt", "r")
            promocodesR = promocodesOPEN.read()
            promocodesOPEN.close()
            act4IN2 = input()
            if (act4IN2 == str(promocodesR) and PromocodeR != str(True)):
                Promocode = open("Promocode.txt", "w")
                Promocode.write(str(True))
                Promocode.close()
                stoneLike = open("stoneLike.txt", "r")
                qwerty123 = stoneLike.read()
                stoneLike.close()
                stoneLike = open("stoneLike.txt", "w")
                stoneLike.write(str(int(qwerty123) + 60))
                stoneLike.close()
                print("ПРомокод активирован!")
            else:
                print("Промокод не найден...")
        if (act4 == str(3)):
            print("ПАРОЛЬ:")
            act4CODE = (input())
            if (act4CODE == "qwe"):
                print("Добавить лайков - 1")
                print("Изменить промокод - 2")
                cmd = int(input())
                if (cmd == 1):
                    stoneLike = open("stoneLike.txt", "r")
                    qwerty123 = stoneLike.read()
                    stoneLike.close()

                    print("Сейчас лайков:", qwerty123)
                    cmd1 = int(input("Сколько лайков? "))

                    stoneLike = open("stoneLike.txt", "w")
                    stoneLike.write(str(int(qwerty123) + cmd1))
                    stoneLike.close()
                    print("Теперь лайков: ", int(qwerty123) + cmd1)

                if (cmd == 2):
                    promocodesOPEN = open("Promocodes.txt", "r")
                    promocodesR = promocodesOPEN.read()
                    promocodesOPEN.close()
                    print("Промокод сейчас:", promocodesR)
                    cmd2 = input("Новый промокод: ")

                    promocodesOPEN = open("Promocodes.txt", "w")
                    promocodesOPEN.write(str(cmd2))
                    promocodesOPEN.close()

                    promocodesOPEN = open("Promocodes.txt", "r")
                    promocodesR = promocodesOPEN.read()
                    promocodesOPEN.close()
                    print("Промокод сейчас: ", promocodesR)

                    Promocode = open("Promocode.txt", "w")
                    Promocode.write("False")
                    Promocode.close()







    else:
        print('')
