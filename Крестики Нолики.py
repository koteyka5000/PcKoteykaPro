from tkinter import *

# TODO change import method

CANVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

# Players
X = 'Player 1'
O = 'Player 2'
FIRST_PLAYER = X


class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    def build_grid(self, grid_color):
        pass

    def render_cross(self, posX, posY):
        pass

    def render_circle(self, posX, posY):
        pass

    def winner(self, player=None):
        pass


game_v1 = Board(start_player=FIRST_PLAYER)

game_v1.mainloop()
