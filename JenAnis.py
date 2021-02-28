from tkinter import *
from math import *

# Создаём окно 485 на 550. Указываем, что окно не будет изменяться.
# Задаем формат вывода, цвета фона
class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

# Создаем массив кнопок, где Х это геометрическая величина 
        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2",
            "P - Прям(a,b)", "S - Прям", "P - Треуг", "S - Треуг",
            "P - Окруж", "S - Окруж",
            "P - Трап", "S - Трап", "a", "Корень", "Квад Ур", "X^Y"
        ]
# Расположение и внешний вид кнопок
        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 12),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81
# Сам Калькулятор
    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "P - Прям(a,b)":
            tmp = self.formula.split('a')
            self.formula = p_prymoygolnik(int(tmp[0]), int(tmp[1]))
        elif operation == "X^Y":
            tmp = self.formula.split('a')
            self.formula = pwr(int(tmp[0]), int(tmp[1]))
        elif operation == "S - Прям":
            tmp = self.formula.split('a')
            self.formula = s_prymoygolnik(int(tmp[0]), int(tmp[1]))
        elif operation == "P - Треуг":
            tmp = self.formula.split('a')
            self.formula = p_treygolnika(int(tmp[0]), int(tmp[1]), int(tmp[2]))
        elif operation == "Квад Ур":
            tmp = self.formula.split('a')
            self.formula = kvadur(int(tmp[0]), int(tmp[1]), int(tmp[2]))
        elif operation == "S - Треуг":
            tmp = self.formula.split('a')
            self.formula = s_treygolnika(int(tmp[0]), int(tmp[1]))
        elif operation == "P - Окруж":
            self.formula = l_kryg(int(self.formula))
        elif operation == "Корень":
            self.formula = sqr(int(self.formula))
        elif operation == "S - Окруж":
            self.formula = s_kryg(int(self.formula))
        elif operation == "P - Трап":
            tmp = self.formula.split('a')
            self.formula = p_trapeciy(int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3]))
        elif operation == "S - Трап":
            tmp = self.formula.split('a')
            self.formula = s_trapeciy(int(tmp[0]), int(tmp[1]), int(tmp[2]))
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)

# Само окно
if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x800+200+200")
    root.title("Продвинутый Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
#ГЕОМЕТРИЯ
def s_prymoygolnik(a, b):
    return (a * b)
def kvadur(a, b, c):
    d = b ** 2 - 4* a * c
    if d < 0:
        return("Нет Решения")
    else:
        x1 = 0
        x2 = 0
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return("x1 = " + str(max(x1,x2)) + '///' + "x2 = " + str(min(x1, x2)))
def sqr(n):
    return sqrt(n)

def pwr(x, y):
    return x ** y

def p_prymoygolnik(a, b):
    return (a + b) * 2            # a, b - стороны

def s_treygolnika(a, h):
    return (a * h / 2)                  # a - сторона, h - высота

def p_treygolnika(a, b, c):
    return (a + b + c)              # a, b, c - стороны

def s_trapeciy(a, b, h):
    return ((((a + b)) / 2) * h)    # a, b  - сторона, h - высота

def p_trapeciy(a, b, c, d):
    return (a + b + c + d)                 # a - сторона

def l_kryg(R):
    return (2 * pi * R)             # R - радиус

def s_kryg(R):
    return (pi * R ** 2)             # R - радиус

