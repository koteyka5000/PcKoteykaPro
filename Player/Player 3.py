from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()


def check_wall(where, self):
    if self.hammer:
        return 1
    print(self.walls)
    xy = self.get_coords()  # (x1, y1, x2, y2) PLayer

    if where == 'w':
        pass
    elif where == 'a':
        pass
    elif where == 's':
        for q, w in self.walls:
            pass

    elif where == 'd':
        pass

    return 1


class Hero:
    def __init__(self):
        self.walls = []
        self.obj = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.x_right = 10
        self.x_left = -10
        self.y_up = -10
        self.y_down = 10
        self.hammer = False

    def hammer_on(self):
        self.hammer = True

    def summon_walls(self):
        walls = []
        for i in range(40):
            x = randint(0, 400)
            y = randint(0, 400)
            canvas.create_oval(x, y, x + 15, y + 15, fill='blue')
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
