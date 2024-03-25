﻿from tkinter import Tk, Button
from tkinter.font import Font
from copy import deepcopy


class Board: #Tạo bàn cờ 

    def __init__(self, other=None): 
        self.player = 'X'
        self.opponent = 'O'
        self.empty = ' '
        self.size = 3
        self.fields = {}
        for y in range(self.size):
            for x in range(self.size):
                self.fields[x, y] = self.empty
    # sao chép hàm constructor dùng thư viện copy 
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def move(self, x, y):
        board = Board(self)
        board.fields[x, y] = board.player
        (board.player, board.opponent) = (board.opponent, board.player)
        return board

    def __minimax_ai(self, player):
        if self.kiemtra_win():
            if player:
                return (-1, None)
            else:
                return (+1, None)
        elif self.ktra_chan():
            return (0, None)
        elif player:
            toiuu_vitri = (-2, None)
            for x, y in self.fields:
                if self.fields[x, y] == self.empty:
                    value = self.move(x, y).__minimax_ai(not player)[0]
                    if value > toiuu_vitri[0]:
                        toiuu_vitri = (value, (x, y))
            return toiuu_vitri
        else:
            toiuu_vitri = (+2, None)
            for x, y in self.fields:
                if self.fields[x, y] == self.empty:
                    value = self.move(x, y).__minimax_ai(not player)[0]
                    if value < toiuu_vitri[0]:
                        toiuu_vitri = (value, (x, y))
            return toiuu_vitri

    def toiuu_vitri(self):
        return self.__minimax_ai(True)[1]

    def ktra_chan(self):
        for (x, y) in self.fields:
            if self.fields[x, y] == self.empty:
                return False
        return True

    def kiemtra_win(self):
        # theo nằm ngang
        for y in range(self.size):
            winning = []
            for x in range(self.size):
                if self.fields[x, y] == self.opponent:
                    winning.append((x, y))
            if len(winning) == self.size:
                return winning
        # theo chiều dọc
        for x in range(self.size):
            winning = []
            for y in range(self.size):
                if self.fields[x, y] == self.opponent:
                    winning.append((x, y))
            if len(winning) == self.size:
                return winning
        # theo đường chéo chính
        winning = []
        for y in range(self.size):
            x = y
            if self.fields[x, y] == self.opponent:
                winning.append((x, y))
        if len(winning) == self.size:
            return winning
        # theo đường chéo phụ
        winning = []
        for y in range(self.size):
            x = self.size-1-y
            if self.fields[x, y] == self.opponent:
                winning.append((x, y))
        if len(winning) == self.size:
            return winning
        # default
        return None



class GUI:

    def __init__(self):
        self.app = Tk()
        self.app.title('Tic-Tac-Toe')
        self.app.resizable(width=False, height=False)
        self.board = Board()
        self.font = Font(family="Roboto", size=34)
        self.buttons = {}
        for x, y in self.board.fields:
            def handler(x=x, y=y): return self.move(x, y)
            button = Button(self.app, command=handler,
                            font=self.font, width=2, height=1)
            button.grid(row=y, column=x)
            self.buttons[x, y] = button

        def handler(): return self.reset()
        button = Button(self.app, text='Ván mới', command=handler)
        button.grid(row=self.board.size+1, column=0,
                    columnspan=self.board.size, sticky="WE")
        self.update()

    def reset(self):
        self.board = Board()
        self.update()

    def move(self, x, y):
        self.app.config(cursor="watch")
        self.app.update()
        self.board = self.board.move(x, y)
        self.update()
        move = self.board.toiuu_vitri()
        if move:
            self.board = self.board.move(*move)
            self.update()
        self.app.config(cursor="")

    def update(self):
        for (x, y) in self.board.fields:
            text = self.board.fields[x, y]
            self.buttons[x, y]['text'] = text
            self.buttons[x, y]['disabledforeground'] = 'black'
            if text == self.board.empty:
                self.buttons[x, y]['state'] = 'normal'
            else:
                self.buttons[x, y]['state'] = 'disabled'
        winning = self.board.kiemtra_win()
        if winning: 
            for x, y in winning:
                self.buttons[x, y]['disabledforeground'] = 'red'
            for x, y in self.buttons:
                self.buttons[x, y]['state'] = 'disabled'
        for (x, y) in self.board.fields:
            self.buttons[x, y].update()

    def mainloop(self):
        self.app.mainloop()


if __name__ == '__main__':
    GUI().mainloop()

