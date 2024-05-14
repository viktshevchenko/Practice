from tkinter import *
from tkinter import ttk

topic1 = "Способы задания булевых функций"
topic2 = "Постоение СКНФ и СДНФ"
topic3 = "Построение полинома Жегалкина"
topics = [topic1, topic2, topic3]

groups = ["ИТПМ-123", "ИТПМ-122", "ИТПМ-121", "ИТПМ-120"]

window = Tk()
window.geometry('405x270')
window.title('Генератор заданий контрольных работ')
window.resizable(0, 0)
window.wm_attributes('-topmost', 1)

group = StringVar(value="ИТПМ-123")
name = StringVar(value =" ")
t1 = IntVar(value=1)
t2 = IntVar(value=1)
t3 = IntVar(value=1)
subj = StringVar()

def validate(new_value):
    return new_value == "" or new_value.isnumeric()

vcmd = (window.register(validate), '%P')

def CreateFail(name, group, t1, t2, t3):
    file = open("info.txt", 'w')
    if name == " ": name = "Преподаватель"
    file.write(f"{subj} {name} {group} {t1} {t2} {t3}")
    file.close()
    window.destroy()

def clear():
    all_widgets = window.place_slaves()
    for l in all_widgets:
        l.destroy()


def subject():
    b_1 = Button(text='Дискретная математика', font=('Arial', 18), fg='black', bg="DarkSeaGreen1", command=lambda: user(1))
    b_1.place(x=55, y=75, width=300)

    b_2 = Button(text='Математический анализ', font=('Arial', 18), bg="DarkSeaGreen1", fg='black', command=lambda: user(2))
    b_2.place(x=55, y=140, width=300)


def user(s):
    b_1 = Button(text='Студент', font=('Arial', 18), fg='black', bg="DarkSeaGreen1", command=student)
    b_1.place(x=55, y=75, width=300)

    b_2 = Button(text='Преподаватель', font=('Arial', 18), bg="DarkSeaGreen1", fg='black', command=teacher)
    b_2.place(x=55, y=140, width=300)

    global subj
    match s:
        case 1:
            subj = "Дискретная математика"
        case 2:
            subj = "Математический анализ"

def student():
    clear()

    Label(window, text="Введите ФИО: ").place(x=30, y=50)
    Entry(window, textvariable=name, validate='key', width=35).place(x=160, y=50)

    common()

def teacher():
    clear()

    ttk.Label(window, text="Группа: ").place(x=30, y=50)
    ttk.Combobox(values=groups, textvariable=group, width=35).place(x=140, y=50)

    common()

def common():
    Label(window, text=topic1).place(x=30, y=90)
    Entry(window, textvariable=t1, validate='key', validatecommand=vcmd).place(x=250, y=90)

    Label(window, text=topic2).place(x=30, y=130)
    Entry(window, textvariable=t2, validate='key', validatecommand=vcmd).place(x=250, y=130)

    Label(window, text=topic3).place(x=30, y=170)
    Entry(window, textvariable=t3, validate='key', validatecommand=vcmd).place(x=250, y=170)

    Button(window, text="Сгенерировать работу", bg="DarkSeaGreen1",
           command=lambda: CreateFail(name.get(), group.get(), t1.get(), t2.get(), t3.get())).place(x=155, y=220)


subject()
window.mainloop()
