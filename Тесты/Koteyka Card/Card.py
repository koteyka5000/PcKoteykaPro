import pickle


def init(num, name, ccv):
    with open('dataCard.bin', 'rb+') as datab:
        data = pickle.load(datab)
        return (num, name, ccv) in data


def writeToCards(w, e, r):
    with open('dataCard.bin', 'rb') as q:  a = pickle.load(q)
    a.append((w, e, r))


def main():
    q = input('Num: ')
    w = input('Name: ')
    e = input('CCV: ')
    gg = init(q, w, e)
    with open('money001.bin', 'rb') as l:
        money = pickle.load(l)
    if gg:
        while 1:
            print('Что делаем?')
            print(f'На счету: {money}')
            print('1 - Перевести деньги')
            what = input('Действие: ')
            if what == '1':
                if input("Вы уверены? (да / нет) ").lower() == "да":
                    moneyq = int(input('Сколько переводим? - '))
                    if moneyq <= money:
                        print(f'УСПЕШНО ПЕРЕВЕДЕНО {moneyq}')
                        w = money - moneyq
                        with open('money001.bin', 'wb') as l:
                            pickle.dump(w, l)
                else:
                    print('!ОТМЕНЕНО!')
    else:
        print('Карта не найдена')
main()