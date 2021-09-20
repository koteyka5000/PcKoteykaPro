from tkinter import *
import random
import time
import keyboard

game_width = 500
game_height = 500
snake_item = 10
snake_color1 = 'red'
snake_color2 = 'yellow'
virtual_game_x = game_width / snake_item
virtual_game_y = game_height / snake_item

snake_x = virtual_game_x // 2
snake_y = virtual_game_y // 2
snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 4

present_color1 = 'blue'
present_color2 = 'black'
presents_list = []
presents_size = 200

tk = Tk()
tk.title('Змейка')
tk['bg'] = 'cyan'
tk.resizable(0, 0)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0, bg='cyan')
canvas.pack()
tk.update()

for i in range(presents_size):
    x = random.randrange(int(virtual_game_x))
    y = random.randrange(int(virtual_game_y))

    id1 = canvas.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item,
                             y * snake_item + snake_item,
                             fill=present_color2)
    id2 = canvas.create_oval(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                             y * snake_item +
                             snake_item - 2, fill=present_color1)

    presents_list.append([x, y, id1, id2])


def snake_paint_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                  y * snake_item + snake_item,
                                  fill=snake_color2)
    id2 = canvas.create_rectangle(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                  y * snake_item +
                                  snake_item - 2, fill=snake_color1)
    snake_list.append([x, y, id1, id2])


def check_delete():
    pass
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        canvas.delete(temp_item[2], temp_item[3])


def check_present():
    global snake_size
    for i in range(len(presents_list)):
        if presents_list[i][0] == snake_x and presents_list[i][1] == snake_y:
            snake_size += 1
            canvas.delete(presents_list[i][2])
            canvas.delete(presents_list[i][3])


xLabel = Label(text=f'X:{snake_x}\nY:{snake_y}\nL:{snake_size}    ', bg='cyan', fg='blue', font='Arial 10')
xLabel.place(x=0, y=0)

Ach1 = True


def snake_move(event):
    global Ach1
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav

    if snake_x == 1000 and snake_y == 1000 and Ach1:
        Label(text='ДОСТИЖЕНИЕ ОТКРЫТО:\nДалёкое прошлое', bg='yellow', font='Bold 15').pack()
        Ach1 = False
    if event.keysym == 'Up':
        snake_x_nav = 0
        snake_y_nav = -1
        check_delete()
    elif event.keysym == 'Down':
        snake_x_nav = 0
        snake_y_nav = 1
        check_delete()
    elif event.keysym == 'Left':
        snake_x_nav = -1
        snake_y_nav = 0
        check_delete()
    elif event.keysym == 'Right':
        snake_x_nav = 1
        snake_y_nav = 0
        check_delete()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    xLabel['text'] = f'X:{snake_x}\nY:{snake_y}\nL:{snake_size}'
    check_present()


snake_paint_item(canvas, snake_x, snake_y)

canvas.bind_all('<KeyPress-Left>', snake_move)
canvas.bind_all('<KeyPress-Right>', snake_move)
canvas.bind_all('<KeyPress-Down>', snake_move)
canvas.bind_all('<KeyPress-Up>', snake_move)

GR = True


def game_over():
    global GR
    GR = False


def check_borders():
    if snake_x > virtual_game_x or snake_x < 0 or snake_y > virtual_game_y or snake_y < 0:
        game_over()


def check_touch(f_x, f_y):
    global GR
    if not (snake_x_nav == 0 and snake_y_nav == 0):
        for i in range(len(snake_list)):
            if snake_list[i][0] == f_x and snake_list[i][1] == f_y:
                print('lol')
                GR = False


def tp():
    global snake_x, snake_y
    snake_x = 10
    snake_y = 10


def lenght():
    global snake_size
    snake_size += 10


keyboard.add_hotkey('q+alt+c', tp)
keyboard.add_hotkey('q+alt+x', lenght)

while GR:
    check_delete()
    check_present()
    check_borders()
    check_touch(snake_x + snake_x_nav, snake_y + snake_y_nav)
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    tk.update_idletasks()
    tk.update()
    xLabel['text'] = f'X:{snake_x}\nY:{snake_y}\nL:{snake_size}    '
    time.sleep(0.1)
tk.mainloop()
