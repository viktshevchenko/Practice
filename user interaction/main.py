from tkinter import *
from tkinter import ttk

topic1 = "Способы задания булевых функций"
topic2 = "Постоение СКНФ и СДНФ"
topic3 = "Построение полинома Жегалкина"
topics = [topic1, topic2, topic3]

window = Tk()
window.geometry('400x270')
window.title('Генератор заданий контрольных работ')
window.resizable(0, 0)
window.wm_attributes('-topmost', 1)


def validate(new_value):
    return new_value == "" or new_value.isnumeric()


def CreateFail(group, topic, options, tasks):
    if topic == topic1:
        t = 1
    elif topic == topic2:
        t = 2
    elif topic == topic3:
        t = 3
    else:
        t = 0
    file = open("info.txt", 'w')
    file.write(f"{group} {t} {options} {tasks}")
    file.close()
    window.destroy()


group = StringVar()
topic = StringVar(value=topics[0])
options = IntVar(value=1)
tasks = IntVar(value=3)

Label(window, text="Дискретная математика").place(x=140, y=10)
Label(window, text="Группа: ").place(x=30, y=50)
ttk.Label(window, text="Выберите тему: ").place(x=30, y=90)
Label(window, text="Количество вариантов").place(x=30, y=130)
Label(window, text="Количество заданий в варианте").place(x=30, y=170)

vcmd = (window.register(validate), '%P')

Entry(window, textvariable=group, validate='key').place(x=240, y=50)
ttk.Combobox(values=topics, state="readonly", textvariable=topic, width=35).place(x=130, y=90)
Entry(window, textvariable=options, validate='key', validatecommand=vcmd).place(x=240, y=130)
Entry(window, textvariable=tasks, validate='key', validatecommand=vcmd).place(x=240, y=170)

Button(window, text="Сгенерировать контрольную работу", bg="DarkSeaGreen1",
       command=lambda: CreateFail(group.get(), topic.get(), options.get(), tasks.get())).place(x=155, y=220)

window.mainloop()
