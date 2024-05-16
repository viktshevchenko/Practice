from tkinter import *
from tkinter import ttk

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