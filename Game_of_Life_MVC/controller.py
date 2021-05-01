from view import Board, Welcome
from model import Model
import tkinter as tk

class Controller:
    def __init__(self, root):
        self.root = root
        self.model = Model(self)
        self.welcome = Welcome(self, root)

    def initiation(self, l, w):
        self.board = Board(self)
        self.model.initiation(l, w)

    def set_btns(self, l, w):
        self.board.set_btns(l, w)

    def set_board(self, i, j, status):
        self.board.set_board(i, j, status)

    def transitioning_generations(self):
        self.model.result()

    def displaying_transition(self, r, c, x):
        self.board.displaying_transition(r, c, x)

if __name__ == '__main__':

    root = tk.Tk()
    Controller(root)
    root.mainloop()
