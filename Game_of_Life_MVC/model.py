import random

class Cell:
    def __init__(self):
        self.status = int()


class Model:
    def __init__(self, controller):
        self.controller = controller

        self.length = 0
        self.width = 0
        self.grid = []
        self.future = []

    def initiation(self, l, w):
        # This method initiates the first generation
        self.controller.set_btns(l, w)
        for i in range(l):
            line = []
            n_line = []
            for j in range(w):
                cell = Cell()
                f_cell = Cell()
                percent = random.randint(0, 100)
                if percent >= 50:
                    cell.status = 1
                    self.controller.set_board(i, j, 1)
                    line.append(cell)
                elif percent < 50:
                    cell.status = 0
                    self.controller.set_board(i, j, 0)
                    line.append(cell)
                n_line.append(f_cell)
            self.grid.append(line)
            self.future.append(n_line)

        for i in  range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print('-' if self.grid[i][j].status == None else self.grid[i][j].status, end='')
            print()

    def transition(self, r, c):
        total_n = 0

        start_r = r - 1
        if start_r < 0:
            start_r = r

        end_r = r + 1
        if end_r == 20:
            end_r = r

        start_c = c - 1
        if start_c < 0:
            start_c = c

        end_c = c + 1
        if end_c == 20:
            end_c = c

        for row in range(start_r, end_r + 1):
            for col in range(start_c, end_c + 1):
                if row == r and col == c:
                    pass
                else:
                    total_n = total_n + self.grid[row][col].status
        return total_n

    def result(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                x = self.transition(r, c)
                if x == 2:
                    self.future[r][c].status = self.grid[r][c].status
                    self.controller.displaying_transition(r, c, x)
                elif x == 3:
                    self.future[r][c].status = 1
                    self.controller.displaying_transition(r, c, x)
                else:
                    self.future[r][c].status = 0
                    self.controller.displaying_transition(r, c, x)
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.grid[r][c] = self.future[r][c]


        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                print('-' if self.grid[r][c].status == None else self.grid[r][c].status, end='')
            print()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                print('-' if self.future[r][c].status == None else self.future[r][c].status, end='')
            print()