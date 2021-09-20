from tkinter import *
import random
import time
try:
    import Koteyka
except:
    print('You dont have module Koteyka on your computer :( Таблица рекордов не будет работать')

inp = ''

def event(key):
    global start
    global inp
    global text
    if inp == '':
        start = time.time()
    key = key.keysym
    if len(key) <= 1 or key == 'BackSpace' or key == 'space' or key == 'period' or key == 'comma' or key == 'question':
        if key == 'space':
            inp += ' '
        elif key == 'BackSpace':
            inp = inp[:-1]
        elif key == 'period':
            inp += '.'
        elif key == 'comma':
            inp += ','
        elif key == 'question':
            inp += '?'
        else:
            inp += key

    else:
        pass
    txt['text'] = inp
    if inp == text:
        print('You win')
        t = '%.3f' % (time.time() - start)
        txt1['text'] = f'You win!\nTime: {t}\nРекорд на этом тексте:\n'


texts = ['Hi, my name is Roman. Im 12 years old. Hope to see you soon.', 'How are you? Im ok, and you? Im ok too',
         'I am going to watch tv this evening', 'Where are you? Im in the garden. Ok.', 'Do you like Minecraft?\
          No, i dont.']
text = random.choice(texts)

root = Tk()
root.bind('<Key>', event)
root.geometry('400x200')
root['bg'] = 'cyan'
txt = Label(text=inp, bg='lemon chiffon')
txt.pack()
txt1 = Label(text=text, bg='lemon chiffon')
txt1.pack(side=TOP)
root.mainloop()
