from random import randint

game = True
num = randint(1, 100)
print(num)
print("Угадай число от 1 до 100")


def log(txt):
    with open('log.log', 'a') as q:
        q.write(txt)
        q.write('\n')


while game:
    guess = int(input('Предпологаемое число: '))
    if guess == num:
        print('Вы угадали!')
        log('Число угадано')
        game = False
    elif guess < num:
        print(f"Ответ неверен, попробуй число больше чем {guess}")
        log('Введено число меньше загаданного')
    elif guess > num:
        print(f'Ответ неверен, попробуй число меньше чем {guess}')
        log("Введено число больше загаданного")
