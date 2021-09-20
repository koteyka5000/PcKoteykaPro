from random import choice


def welcome_speech(t):
    print(f"""
    Добро пожаловать в игру!
    Ваша задача - угадать слово за несколько попыток,
    иначе Вы проиграете! :(
    загаданное слово состоит из {len(t)} букв
    """)


def start_template(w):
    return list('_' * len(w))


def list_to_string_convert(t):
    return ''.join(t)


def get_word(w):
    return choice(w)


def replace(inp, word, template):
    if word.count(inp) == 1:
        template[word.index(inp)] = inp
    else:
        for i in range(len(word)):
            if inp == word[i]:
                template[i] = inp
    return template


def game():
    progress = True
    words = ['яблоко', "вишня", "банан", "киви", "апельсин", "персик"]
    lives = 3

    word_in_play = get_word(words)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    while progress:
        print('=====================')
        print(f'У вас осталось попыток: {lives}')
        print(f'Сейчас слово: {list_to_string_convert(template)}')
        inp = input('Введите предпологаемую букву: ')
        if inp in word_in_play:
            template = replace(inp, word_in_play, template)
        else:
            print('Такой буквы в слове нет :(')
            lives -= 1
        if lives == 0 or word_in_play == list_to_string_convert(template):
            progress = False
    print('\n=+=+=+=+=+=+=+=+=+=+=+=+')
    if lives == 0:
        print(f'Вы хорошо держались :)\nЗагаданым словом было {word_in_play}')
    elif word_in_play == list_to_string_convert(template):
        print(f'Вы победили!! :)\nУ вас осталось попыток: {lives}')
    print('Made by Koteyka')
    print('=+=+=+=+=+=+=+=+=+=+=+=+')


game()
