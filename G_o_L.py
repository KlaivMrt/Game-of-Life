import random

class Generations:
    def __init__(self):
        self.grid = []
        self.future = []
        self.status = int()

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
                print('-' if self.grid[i][j] == 0 else self.grid[i][j], end='')
            print()

    def display_f(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print('-' if self.future[i][j] == 0 else self.future[i][j], end='')
            print()


    def initiation(self, w, l):
        for i in range(l):
            line = []
            n_line = []
            for j in range(w):
                percent = random.randint(0, 100)
                if percent >= 50:
                    self.status = 1
                    line.append(self.status)
                elif percent < 50:
                    self.status = 0
                    line.append(self.status)
                n_line.append(0)
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
                if row == r and col == c:
                    pass
                else:
                    total_n = total_n + self.grid[row][col]
        return total_n

    def result(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                x = self.transition(r, c)
                if x == 2:
                    self.future[r][c] = self.grid[r][c]
                elif x == 3:
                    self.future[r][c] = 1
                else:
                    self.future[r][c] = 0
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
