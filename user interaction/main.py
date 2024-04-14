from tkinter import *

window = Tk()
window.geometry('400x250')
window.title('Генератор заданий контрольных работ')
window.resizable(0, 0)
window.wm_attributes('-topmost', 1)


def validate(new_value):
    return new_value == "" or new_value.isnumeric()


def CreateFail(topic, options, tasks):
    file = open("info.txt", 'w')
    file.write(f"{topic} {options} {tasks}")
    file.close()
    window.destroy()


topic = IntVar(value=1)
options = IntVar(value=1)
tasks = IntVar(value=3)

Label(window, text="Дискретная математика").place(x=140, y=10)
Label(window, text="Введите номер темы: ").place(x=30, y=50)
Label(window, text="Количество вариантов").place(x=30, y=90)
Label(window, text="Количество заданий в варианте").place(x=30, y=130)

vcmd = (window.register(validate), '%P')

Entry(window, textvariable=topic, validate='key', validatecommand=vcmd).place(x=220, y=50)
Entry(window, textvariable=options, validate='key', validatecommand=vcmd).place(x=220, y=90)
Entry(window, textvariable=tasks, validate='key', validatecommand=vcmd).place(x=220, y=130)

Button(window, text="Сгенерировать контрольную работу", bg="DarkSeaGreen1", command=lambda: CreateFail(topic.get(), options.get(), tasks.get())).place(x=30, y=200)

window.mainloop()