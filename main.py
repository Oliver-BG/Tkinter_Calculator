from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("./calclogo.ico")

class Calculator():
    def __init__(self, master):
        """Sets the attribute for the calculator."""
        self.master = master
        self.entry1 = Entry(self.master, bg = "white", borderwidth = 2, font = (None, 24))
        self.entry2 = Entry(self.master, bg = "white", borderwidth = 2, font = (None, 24))
        self.add = Button(self.master, text = "+", padx = 60, pady = 30, command = lambda: calc_op(calc, "+"))
        self.subtract = Button(self.master, text = "_", padx = 60, pady = 30, command =lambda: calc_op(calc, "-"))
        self.multiply = Button(self.master, text="x", padx = 60, pady = 30, command = lambda: calc_op(calc, "x"))
        self.divide = Button(self.master, text="/", padx = 60, pady = 30, command = lambda: calc_op(calc, "/"))
        self.clear = Button(self.master, text = "CLEAR", padx = 114, pady = 30, command = lambda: calc_clear(calc))
        self.equal = Button(self.master, text = "=", padx = 126, pady = 30, command = lambda: calc_eq(calc))
        self.entry_list = []
        self.button_list = [self.add, self.subtract, self.multiply, self.divide]
        self.flag = False
        self.entry_flag = False

    def add_widgets(self):
        """Adds the widgets on the master window."""
        self.entry1.grid(row = 0, columnspan = 3, sticky = [W,E])
        self.entry2.grid(row = 1, columnspan = 3, sticky = [W,E])
        self.equal.grid(row = 5, column = 1, columnspan = 2)
        self.add.grid(row = 6, column = 0)
        self.clear.grid(row = 6, column = 1, columnspan = 2)
        self.multiply.grid(row = 7, column = 0)
        self.subtract.grid(row = 7, column = 1)
        self.divide.grid(row = 7, column = 2)

    def add_numeric_button(self):
        """Adds numeric buttons in the master window."""
        n = 0
        for i in range(1,10):
            if i <= 3:
                button = Button(self.master, text = i, padx = 60, pady = 30, command = lambda i=i: add_num(calc, i))
                button.grid(row = 4, column = n % 3)
            elif i <= 6:
                button = Button(self.master, text=i, padx = 60, pady = 30, command = lambda i=i: add_num(calc, i))
                button.grid(row = 3, column = n % 3)
            else:
                button = Button(self.master, text = i, padx = 60, pady = 30, command = lambda i=i: add_num(calc, i))
                button.grid(row = 2, column = n % 3)
            n += 1

            button_0 = Button(self.master, text = 0, padx = 60, pady = 30, command = lambda: add_num(calc, 0))
            button_0.grid(row = 5, column = 0)

### FUNCTIONS ###
def add_num(calc, number):
    """Adds number to the entry box."""
    if calc.entry_flag:
        calc.entry2.delete(0, END)
        calc.entry_flag = False
    calc.entry2.insert(END, str(number))
    switch_on(calc)

def switch_off(calc):
    """Disables an operator after clicking. This would resolve some issues of value errors."""
    if calc.flag:
        for button in calc.button_list:
            if button['state'] == NORMAL:
                button.config(state = DISABLED)

def switch_on(calc):
    """Switches operator into normal status after they click a number."""
    calc.flag = False
    if not calc.flag:
        for button in calc.button_list:
            if button['state'] == DISABLED:
                button.config(state = NORMAL)

def add_zero(calc):
    """Adds zero to the secondary entry and equation list if the user
        clicks the operators first."""
    if len(calc.entry2.get()) == 0:
        calc.entry_list.insert(0, str(0))
        calc.entry1.insert(END, str(0))

def calc_op(calc, op):
    """Adds an operator in the entry and equation list."""
    add_zero(calc)
    value = calc.entry2.get()
    calculate(calc)
    operator = op
    calc.entry_list.append(operator)
    calc.entry1.insert(END, f"{str(value)} {operator} ")
    switch_off(calc)

def calculate(calc):
    """Calculates the entire equation."""
    calc.entry_list.append(calc.entry2.get())
    calc.entry2.delete(0, END)
    calc.flag = True
    calc.entry_flag = True

    try:
        init_value = float(calc.entry_list[0])
        for i in range(len(calc.entry_list)):
            if calc.entry_list[i] == "+":
                init_value += float(calc.entry_list[i + 1])
            elif calc.entry_list[i] == "-":
                init_value -= float(calc.entry_list[i + 1])
            elif calc.entry_list[i] == "x":
                init_value *= float(calc.entry_list[i + 1])
            elif calc.entry_list[i] == "/":
                init_value /= float(calc.entry_list[i + 1])
    except ZeroDivisionError:
        calc.entry1.delete(0, END)
        calc.entry1.insert(END, "Undefined.")
        calc.entry_list.clear()
    except Exception:
        calc.entry1.delete(0, END)
        calc.entry1.insert(END, "Value error. Please try again.")
        calc.entry_list.clear()
    else:
        calc.entry2.insert(END, str(init_value))

def calc_eq(calc):
    """Provides the result of the whole equation"""
    calc.entry1.delete(0, END)
    calculate(calc)
    switch_on(calc)

def calc_clear(calc):
    """Clears the entire entry and lists."""
    calc.entry_list.clear()
    calc.entry1.delete(0, END)
    calc.entry2.delete(0, END)
    switch_on(calc)

calc = Calculator(root)
calc.add_widgets()
calc.add_numeric_button()
root.mainloop()
