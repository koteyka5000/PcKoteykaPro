
from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()


def check_wall(where, self):
    if self.hammer:
        return 1
    for w in self.walls:
        wx1 = w[0]
        wx2 = w[0] + 15
        wy1 = w[1]
        wy2 = w[1] + 15
        sx1, sy1, sx2, sy2 = self.get_coords()  # (x1, y1, x2, y2) PLayer

        if where == 'd':
            if sx2 + 5 > wx1 and sx1 + 5 < wx2 and sy2 > wy1 and sy1 < wy2:
                return 0

        if where == 'w':
            if sx2 > wx1 and sx1 < wx2 and sy2 - 5 > wy1 and sy1 - 5 < wy2:
                return 0

        elif where == 'a':
            if sx2 - 5 > wx1 and sx1 - 5 < wx2 and sy2 > wy1 and sy1 < wy2:
                return 0

        elif where == 's':
            if sx2 > wx1 and sx1 < wx2 and sy2 + 5 > wy1 and sy1 + 5 < wy2:
                return 0
        print('---')

    return 1


class Hero:
    def __init__(self):
        self.walls = []
        self.obj = canvas.create_rectangle(10, 10, 25, 25, fill='red')
        self.x_right = 5
        self.x_left = -5
        self.y_up = -5
        self.y_down = 5
        self.hammer = False

    def hammer_on(self):
        self.hammer = True

    def summon_walls(self):
        walls = []
        for i in range(1):
            x = 15 * randint(0, 25)
            y = 15 * randint(0, 25)
            canvas.create_rectangle(x, y, x + 15, y + 15, fill='blue')
            walls.append((x, y))  # x + 15, y + 15
        self.walls = walls

    def move_right(self, event):
        if check_wall('d', self):
            canvas.move(self.obj, self.x_right, 0)

    def move_left(self, event):
        if check_wall('a', self):
            canvas.move(self.obj, self.x_left, 0)

    def move_up(self, event):
        if check_wall('w', self):
            canvas.move(self.obj, 0, self.y_up)

    def move_down(self, event):
        if check_wall('s', self):
            canvas.move(self.obj, 0, self.y_down)

    def get_coords(self):
        return canvas.coords(self.obj)


hero = Hero()

canvas.bind_all('<KeyPress-d>', hero.move_right)
canvas.bind_all('<KeyPress-a>', hero.move_left)
canvas.bind_all('<KeyPress-w>', hero.move_up)
canvas.bind_all('<KeyPress-s>', hero.move_down)
hero.summon_walls()

root.update()
root.mainloop()