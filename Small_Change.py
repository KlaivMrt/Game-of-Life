import random

class Cell:
    def __init__(self):
        self.status = int()

class Generations:
    def __init__(self):
        self.grid = []
        self.future = []

    def get_value(self):
        repeat = True
        while repeat:
            try:
                number = int(input('>> >> >> '))
                if number > 0:
                    repeat = False
                    return number

                else:
                    print('The value is too small. Try again!')
            except ValueError:
                print('You have typed an invalid input. Please try again!')

    def get_random(self):
        number = random.randint(30, 50)
        return number

    def display(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print('-' if self.grid[i][j].status == 0 else self.grid[i][j].status, end='')
            print()

    def initiation(self, w, l):
        for i in range(l):
            line = []
            n_line = []
            for j in range(w):
                cell = Cell()
                f_cell = Cell()
                percent = random.randint(0, 100)
                if percent >= 50:
                    cell.status = 1
                    line.append(cell)
                elif percent < 50:
                    cell.status = 0
                    line.append(cell)
                n_line.append(f_cell)
            self.grid.append(line)
            self.future.append(n_line)


    def transition(self, r, c):
        total_n = 0

        start_r = r - 1
        if start_r == 0:
            start_r = r

        end_r = r + 1
        if end_r == l:
            end_r = r

        start_c = c - 1
        if start_c == 0:
            start_c = c

        end_c = c + 1
        if end_c == w:
            end_c = c

        for row in range(start_r, end_r + 1):
            for col in range(start_c, end_c + 1):
                if row == col:
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
                elif x == 3:
                    self.future[r][c].status = 1
                else:
                    self.future[r][c].status = 0
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.grid[r][c] = self.future[r][c]

if __name__ == '__main__':

    b = Generations()

    print('Chose your width')
    w = b.get_value()

    print('Chose your length')
    l = b.get_value()

    b.initiation(w, l)
    b.display()
    print()

    regenarate = 'y'
    while regenarate == 'y':
        b.result()
        b.display()
        print()
        regenarate = input("Next???  y/n  > ")

