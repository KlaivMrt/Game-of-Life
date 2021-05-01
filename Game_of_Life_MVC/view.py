import tkinter as tk

class Welcome:
    def __init__(self, controller, root):
        self.controller = controller

        self.label = tk.Label(root, text='GAME OF LIFE')
        self.btn = tk.Button(root, text='Let\'s start!',
                             command= lambda : [self.controller.initiation(20, 20), self.disabled()])

        self.label.pack()
        self.btn.pack()
        self.get_welcome()

    def get_welcome(self):
        with open('welcome.txt', 'r') as file:
            read = file.read()
            self.label['text'] = read

    def disabled(self):
        self.btn['state'] = 'disabled'

class Board:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Toplevel()
        self.root.resizable(False, False)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.options = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Options', menu=self.options)

        self.options.add_command(label='Start', command=self.start_transitioning)
        self.options.add_command(label='Quit', command=self.controller.root.destroy)

        self.btns = []

        self.generate_next = True



    def set_btns(self, l, w):
        for i in range(l):
            list=[]
            for j in range(w):
                btn = tk.Button(self.root, width=2, height=1)
                list.append(btn)
            self.btns.append(list)

    def set_board(self, i, j, status):
        if status == 1:
            self.btns[i][j]['bg'] = 'blue'
        else:
            self.btns[i][j]['bg'] = 'black'
        self.btns[i][j].grid(row=i, column=j)

    def start_transitioning(self):
        self.controller.transitioning_generations()
        self.root.after(1000, self.start_transitioning)


    def displaying_transition(self, r, c, x):
        if x == 2:
            pass
        elif x == 3:
            self.btns[r][c]['bg'] = 'blue'
        else:
            self.btns[r][c]['bg'] = 'black'



