from tkinter import *
from tkinter import ttk
import random

subject1 = "Дискретная математика"
subject2 = "Математический анализ"

sub1_topic1 = "Способы задания булевых функций"
sub1_topic2 = "Постоение СКНФ и СДНФ"
sub1_topic3 = "Построение полинома Жегалкина"
sub1_topics = [sub1_topic1, sub1_topic2, sub1_topic3]

sub2_topic1 = "Производная от полинома"
sub2_topic2 = "Производная от полинома в точке"
sub2_topic3 = "Геометрический смысл производной"
sub2_topics = [sub2_topic1, sub2_topic2, sub2_topic3]

groups = ["ИТПМ-123", "ИТПМ-122", "ИТПМ-121", "ИТПМ-120"]

window = Tk()
window.geometry('405x300')
window.title('Генератор заданий контрольных работ')
window.resizable(0, 0)
window.wm_attributes('-topmost', 1)

group = StringVar(value="ИТПМ-123")
name = StringVar(value="") #student's name
theme1 = IntVar(value=1) #number of tasks of topic1
theme2 = IntVar(value=1) #number of tasks of topic2
theme3 = IntVar(value=1) #number of tasks of topic3
count1 = IntVar(value=2) #number of variables of topic1
count2 = IntVar(value=2) #number of variables of topic2
count3 = IntVar(value=2) #number of variables of topic3
subject = StringVar()

variable_2 = ['x', 'y']
variable_3 = ['x', 'y', 'z']
variable_4 = ['x', 'y', 'z', 't']

boolean_operations = ['<=', '==', '&', '|', '^']
sign = ['', '~']

def validate(new_value):
    return new_value == "" or new_value.isnumeric()

vcmd = (window.register(validate), '%P')

def check():
    if name.get() == "":
        student_err()
    else:
        CreateFail()
        #window.destroy()

def CreateFail():
    file = open("info.txt", 'w')
    file.write(f"{subject} {name.get()} {group.get()}\n"
               f"{theme1.get()} {count1.get()}\n"
               f"{theme2.get()} {count2.get()}\n"
               f"{theme3.get()} {count3.get()}\n")
    file.close()
    window.destroy()

def clear():
    all_widgets = window.place_slaves()
    for l in all_widgets:
        l.destroy()

def subjects():
    b_1 = Button(text=subject1, font=('Arial', 18), fg='black', bg="DarkSeaGreen1", command=lambda: user(1))
    b_1.place(x=55, y=75, width=300)

    b_2 = Button(text=subject2, font=('Arial', 18), bg="DarkSeaGreen1", fg='black', command=lambda: user(2))
    b_2.place(x=55, y=140, width=300)

def user(s):
    b_1 = Button(text='Студент', font=('Arial', 18), fg='black', bg="DarkSeaGreen1", command=student)
    b_1.place(x=55, y=75, width=300)

    b_2 = Button(text='Преподаватель', font=('Arial', 18), bg="DarkSeaGreen1", fg='black', command=teacher)
    b_2.place(x=55, y=140, width=300)

    global subject
    match s:
        case 1:
            subject = subject1
        case 2:
            subject = subject2

def student():
    clear()

    Label(window, text="Введите ФИО: ").place(x=30, y=20)
    Entry(window, textvariable=name, validate='key', width=35).place(x=160, y=20)

    group.set("")

    common()
    Button(window, text="Сгенерировать работу", bg="DarkSeaGreen1", width=19, command=check).place(x=140, y=240)

def student_err():
    clear()

    Label(window, text="Введите ФИО: ", fg='red').place(x=30, y=20)
    Entry(window, textvariable=name, validate='key', width=35).place(x=160, y=20)

    group.set("")

    common()
    Button(window, text="Сгенерировать работу", bg="DarkSeaGreen1", width=19, command=check).place(x=140, y=240)

def teacher():
    clear()

    ttk.Label(window, text="Группа: ").place(x=30, y=20)
    ttk.Combobox(values=groups, textvariable=group, width=35).place(x=140, y=20)

    name.set("Преподаватель")

    common()
    Button(window, text="Сгенерировать работу", bg="DarkSeaGreen1", width=19, command=CreateFail).place(x=140, y=240)

def themes_subj1():
    Label(window, text="Кол-во\n переменных").place(x=310, y=50)

    Label(window, text=sub1_topic1).place(x=30, y=100)
    Label(window, text=sub1_topic2).place(x=30, y=140)
    Label(window, text=sub1_topic3).place(x=30, y=180)

    ttk.Combobox(values=["2", "3", "4"], textvariable=count1, width=8).place(x=320, y=100)
    ttk.Combobox(values=["2", "3", "4"], textvariable=count2, width=8).place(x=320, y=140)
    ttk.Combobox(values=["2", "3", "4"], textvariable=count3, width=8).place(x=320, y=180)

def themes_subj2():
    Label(window, text="Наивысшая\n степень").place(x=320, y=50)

    Label(window, text=sub2_topic1).place(x=30, y=100)
    Label(window, text=sub2_topic2).place(x=30, y=140)
    Label(window, text=sub2_topic3).place(x=30, y=180)

    Entry(window, textvariable=count1, validate='key', validatecommand=vcmd, width=8).place(x=320, y=100)
    Entry(window, textvariable=count2, validate='key', validatecommand=vcmd, width=8).place(x=320, y=140)
    Entry(window, textvariable=count3, validate='key', validatecommand=vcmd, width=8).place(x=320, y=180)

def common():
    if subject == subject1:
        themes_subj1()
    elif subject == subject2:
        themes_subj2()

    Label(window, text="Кол-во\n заданий").place(x=245, y=50)
    Entry(window, textvariable=theme1, validate='key', validatecommand=vcmd, width=7).place(x=250, y=100)
    Entry(window, textvariable=theme2, validate='key', validatecommand=vcmd, width=7).place(x=250, y=140)
    Entry(window, textvariable=theme3, validate='key', validatecommand=vcmd, width=7).place(x=250, y=180)


subjects()
window.mainloop()

def generate_function(count_var):
    function = ""
    var_last = ''
    match count_var:
        case 2:
            for i in range(random.randint(3, 8)):
                negation = random.choice(sign)
                var = random.choice(variable_2)
                while var == var_last:
                    var = random.choice(variable_2)
                var_last = var
                function += negation + var + " "
                op = random.choice(boolean_operations)
                function += op + " "
        case 3:
            for i in range(random.randint(3, 10)):
                negation = random.choice(sign)
                var = random.choice(variable_3)
                while var == var_last:
                    var = random.choice(variable_2)
                var_last = var
                function += negation + var + " "
                op = random.choice(boolean_operations)
                function += op + " "
        case 4:
            for i in range(random.randint(3, 12)):
                negation = random.choice(sign)
                var = random.choice(variable_2)
                while var == var_last:
                    var = random.choice(variable_4)
                var_last = var
                function += negation + var + " "
                op = random.choice(boolean_operations)
                function += op + " "
        case _:
            if count_var < 2:
                return generate_function(2)
            elif count_var > 4:
                return generate_function(4)
    function = function[:-3]
    value_bool_func = truth_table(str(function), count_var)

    while (not '0' in value_bool_func) or (not '1' in value_bool_func) or '-' in value_bool_func:
        function = generate_function(count_var)
        value_bool_func = truth_table(str(function), count_var)
    return function

def truth_table(func, count_var):
    value = ''
    match count_var:
        case 2:
            #print('x y f')
            for x in range(2):
                for y in range(2):
                    f = eval(func)
                    #print(x, y, int(f))
                    value += str(int(f))
        case 3:
            #print('x y z f')
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        f = eval(func)
                        #print(x, y, z, int(f))
                        value += str(int(f))
        case 4:
            #print('x y z t f')
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        for t in range(2):
                            f = eval(func)
                            #print(x, y, z, t, int(f))
                            value += str(int(f))
        case _:
            if count_var < 2:
                return truth_table(func, 2)
            elif count_var > 4:
                return truth_table(func, 4)
    return value

def sdnf(bool_func, count_var):
    value_bool_func = truth_table(str(bool_func), count_var)
    result = ''
    i = 0
    match count_var:
        case 2:
            for x in range(2):
                for y in range(2):
                    if value_bool_func[i] == '0':
                        result += '('
                        if x == 0:
                            result += 'x & '
                        elif x == 1:
                            result += '~x & '
                        if y == 0:
                            result += 'y'
                        elif y == 1:
                            result += '~y'
                        result += ') | '
                    i += 1
        case 3:
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        if value_bool_func[i] == '0':
                            result += '('
                            if x == 0:
                                result += 'x & '
                            elif x == 1:
                                result += '~x & '
                            if y == 0:
                                result += 'y & '
                            elif y == 1:
                                result += '~y & '
                            if z == 0:
                                result += 'z'
                            elif z == 1:
                                result += '~z'
                            result += ') | '
                        i += 1
        case 4:
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        for t in range(2):
                            if value_bool_func[i] == '0':
                                result += '('
                                if x == 0:
                                    result += 'x & '
                                elif x == 1:
                                    result += '~x & '
                                if y == 0:
                                    result += 'y & '
                                elif y == 1:
                                    result += '~y & '
                                if z == 0:
                                    result += 'z & '
                                elif z == 1:
                                    result += '~z & '
                                if t == 0:
                                    result += 't'
                                elif t == 1:
                                    result += '~t'
                                result += ') | '
                            i += 1
    return result[:-3]

def sknf(bool_func, count_var):
    value_bool_func = truth_table(str(bool_func), count_var)
    result = ''
    i = 0
    match count_var:
        case 2:
            for x in range(2):
                for y in range(2):
                    if value_bool_func[i] == '1':
                        result += '('
                        if x == 1:
                            result += 'x | '
                        elif x == 0:
                            result += '~x | '
                        if y == 1:
                            result += 'y'
                        elif y == 0:
                            result += '~y'
                        result += ') & '
                    i += 1
        case 3:
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        if value_bool_func[i] == '1':
                            result += '('
                            if x == 1:
                                result += 'x | '
                            elif x == 0:
                                result += '~x | '
                            if y == 1:
                                result += 'y | '
                            elif y == 0:
                                result += '~y | '
                            if z == 1:
                                result += 'z'
                            elif z == 0:
                                result += '~z'
                            result += ') & '
                        i += 1
        case 4:
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        for t in range(2):
                            if value_bool_func[i] == '1':
                                result += '('
                                if x == 1:
                                    result += 'x | '
                                elif x == 0:
                                    result += '~x | '
                                if y == 1:
                                    result += 'y | '
                                elif y == 0:
                                    result += '~y | '
                                if z == 1:
                                    result += 'z | '
                                elif z == 0:
                                    result += '~z | '
                                if t == 1:
                                    result += 't'
                                elif t == 0:
                                    result += '~t'
                                result += ') & '
                            i += 1
    return result[:-3]

def polinom_Zhegalkina(bool_func, count_var):
    value_bool_func = truth_table(str(bool_func), count_var)
    func_sdnf = sdnf(value_bool_func, count_var)
    if '~x' in func_sdnf:
        func_sdnf = func_sdnf.replace('~x', '(1 ^ x)')
    if '~y' in func_sdnf:
        func_sdnf = func_sdnf.replace('~y', '(1 ^ y)')
    if '~z' in func_sdnf:
        func_sdnf = func_sdnf.replace('~z', '(1 ^ z)')
    if '~t' in func_sdnf:
        func_sdnf = func_sdnf.replace('~t', '(1 ^ t)')
    if '|' in func_sdnf:
        func_sdnf = func_sdnf.replace('|', '^')
    return func_sdnf


if subject == subject1:
    for i in range(theme1.get()): # генерирует 1ую тему
        bool_func = generate_function(count1.get()) # задание
        value_bool_func = truth_table(str(bool_func), count1.get()) # ответ
        # здесь можно с ними что-то делать (например, записывать в бд или в теховский файл
        # проверка
        """file = open("1.txt", 'a')
        file.write(f"{i+1}. {bool_func}\n"
                   f"{value_bool_func}\n\n")
        file.close()"""

    for i in range(theme2.get()): # генерирует 2ую тему
        bool_func = generate_function(count2.get()) # задание
        SKNF = sknf(bool_func, count2.get()) # ответ
        SDNF = sdnf(bool_func, count2.get())  # ответ
        # здесь можно с ними что-то делать (например, записывать в бд или в теховский файл
        # проверка
        """file = open("2.txt", 'a')
        file.write(f"{i+1}. {bool_func}\n"
                   f"{SKNF}\n"
                   f"{SDNF}\n\n")
        file.close()"""

    for i in range(theme3.get()): # генерирует 3ью тему
        bool_func = str(generate_function(count3.get())) # задание
        polinom = polinom_Zhegalkina(bool_func, count3.get()) # ответ
        # здесь можно с ними что-то делать (например, записывать в бд или в теховский файл
        # проверка
        """file = open("3.txt", 'a')
        file.write(f"{i+1}. {bool_func}\n"
                   f"{polinom}\n\n")
        file.close()"""
