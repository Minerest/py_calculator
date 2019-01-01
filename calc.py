import tkinter as tk


'''Simple calculator GUI using classes and TKINTER'''

class Window(tk.Frame):


    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.calculator = Calculator()
        self.master = master
        self.grid(row=0, column=0, rowspan=9, columnspan=9)
        self.init_window()


    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI")
        self.make_buttons()
        self.make_title_text()
        self.make_calc_text()

    def make_title_text(self):
        self.title_text = tk.Label(self, text='calculator!')
        self.title_text.grid(row=0, column=2)

    def make_calc_text(self):
        '''init function'''

        self.calc_text_var = tk.StringVar()
        self.calc_text_var.set(self.calculator.left)
        self.calc_text = tk.Label(self, textvar=self.calc_text_var, font=('Helvetica', 24), anchor='w')
        self.calc_text.grid(row=1, column=0, rowspan=2, columnspan=99, ipady=50, ipadx=200, sticky='nsew')
        self.calc_text.configure(background="#ffffcc")

    def update_calc_text(self, num):
        if self.calculator.answer_flag:
            self.calculator.clear(self)
        if self.calculator.state == "LEFT":
            self.calculator.update_left(num)
        elif self.calculator.state == "RIGHT":
            self.calculator.update_right(num)

        calc_text = str(self.calculator.left)
        if self.calculator.command is not '':
            calc_text += self.calculator.command
            calc_text += str(self.calculator.right)
        self.calc_text_var.set(calc_text)

    def display_ans(self):
        self.calc_text_var.set(self.calculator.answer)

    def make_buttons(self):
        '''Creates all the buttons in the calculator'''

        button_quit = tk.Button(self, text="Quit", command=self.client_exit)
        button_quit.grid(row=10, column=10)
        button_quit.grid_anchor('se')

        button_add = tk.Button(self, text='+', command=lambda: self.calculator.add_command('+'))
        button_add.grid(row=6, column=8, sticky='nswe')

        button_minus = tk.Button(self, text='-', command=lambda: self.calculator.add_command('-'))
        button_minus.grid(row=6, column=9,sticky='nswe')

        button_div = tk.Button(self, text='/', command=lambda: self.calculator.add_command('/'))
        button_div.grid(row=7, column=8,sticky='nswe')

        button_mult = tk.Button(self, text='*', command=lambda: self.calculator.add_command('*'))
        button_mult.grid(row=7, column=9,sticky='nswe')

        button_one = tk.Button(self, text='1', command=lambda: self.update_calc_text(1))
        button_one.grid(row=5, column=2,sticky='nswe')

        button_two = tk.Button(self, text='2', command=lambda: self.update_calc_text(2))
        button_two.grid(row=5, column=3,sticky='nswe')

        button_three = tk.Button(self, text='3', command=lambda: self.update_calc_text(3))
        button_three.grid(row=5, column=4,sticky='nswe')

        button_four = tk.Button(self, text='4', command=lambda: self.update_calc_text(4))
        button_four.grid(row=6, column=2,sticky='nswe')

        button_five = tk.Button(self, text='5', command=lambda: self.update_calc_text(5))
        button_five.grid(row=6, column=3,sticky='nswe')

        button_six = tk.Button(self, text='6', command=lambda: self.update_calc_text(6))
        button_six.grid(row=6, column=4,sticky='nswe')

        button_sev = tk.Button(self, text='7', command=lambda: self.update_calc_text(7))
        button_sev.grid(row=7, column=2,sticky='nswe')

        button_eight = tk.Button(self, text='8', command=lambda: self.update_calc_text(8))
        button_eight.grid(row=7, column=3,sticky='nswe')

        button_nine = tk.Button(self, text='9', command=lambda: self.update_calc_text(9))
        button_nine.grid(row=7, column=4,sticky='nswe')

        button_zero = tk.Button(self, text='0', command=lambda: self.update_calc_text(0))
        button_zero.grid(row=8, column=3,sticky='nswe')

        button_dot = tk.Button(self, text='.')
        button_dot.grid(row=8, column=2,sticky='nswe')

        button_delete = tk.Button(self, text= 'CLR', command=lambda: self.calculator.clear(self))
        button_delete.grid(row=8, column=4,sticky='nswe')

        button_equals = tk.Button(self, text='=', command=lambda: self.calculator.calculate(self))
        button_equals.grid(row=8, column=8, columnspan=2,sticky='nswe')

    def client_exit(self):
        exit()

class Calculator():

    def __init__(self):
        self.left = 0
        self.left_float = 0
        self.left_length = 0
        self.right = 0
        self.right_float = 0
        self.right_length = 0
        self.answer = 0.0
        self.state = 'LEFT' # to determine which side to change
        self.command = ''
        self.answer_flag = False

    def add(self):
        self.answer = self.left + self.right
    def subtract(self):
        self.answer = self.left - self.right
    def mult(self):
        self.answer = self.left * self.right
    def div(self):
        if self.right == 0:
            return
        self.answer = self.left / self.right

    def clear(self, frame):
        self.left = 0
        self.left_float = 0
        self.left_length = 0
        self.right = 0
        self.right_float = 0
        self.right_length = 0
        self.answer = 0.0
        self.state = 'LEFT' # to determine which side to change
        self.command = ''
        self.answer_flag = False
        frame.update_calc_text(0)

    def update_left(self, num):
        self.left = str(self.left) + str(num)
        self.left = int(self.left)

    def update_right(self, num):
        self.right = int(str(self.right) + str(num))

    def alternate_side(self):
        '''used to determine which side the calculator starts updating'''
        if self.state == "LEFT":
            self.state = "RIGHT"

    def add_command(self, command):

        self.command = command
        self.alternate_side()

    def calculate(self, frame):

        if self.answer_flag:
            self.left = self.answer

        if self.command == '':
            return
        elif self.command == '+':
            self.add()
        elif self.command == '-':
            self.subtract()
        elif self.command == '/':
            self.div()
        else:
            self.mult()
        self.answer_flag = True
        frame.display_ans()


def main():
    root = tk.Tk()
    root.geometry("450x500")
    root.resizable(False, False)
    app = Window(root)
    root.mainloop()


main()
