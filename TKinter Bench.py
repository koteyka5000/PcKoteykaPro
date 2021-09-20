from tkinter import *
# from threading import Thread
# import time
# import random
from multiprocessing import *


root = Tk()
root.geometry('300x200')


def Test():
    def Test1():
        print("d")
        global root
        root['bg'] = 'red'

    if __name__ == '__main__':
        Process(target=Test1).start()


Button(text=123, command=Test).pack()
root.mainloop()
