from reportlab.pdfgen import canvas  # pip install reportlab
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

from datetime import date

subject = "Дискретная математика"  # название предмета
students_name = "ФИО"  # из бд
center = 230
start = 100
top = 790
interval = 22

pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))  # Загружаем шрифт с поддержкой кириллицы

doc_for_teacher = canvas.Canvas("Ответы.pdf")  # Создаем новый PDF файл
doc_for_teacher.setFont("Arial", 12)  # Устанавливаем текущий шрифт
doc_for_teacher.drawString(500, 790, date.today().strftime("%d.%m.%Y"))  # Добавляем дату
doc_for_teacher.drawString(center, 790, subject)  # Добавляем название предмета

# начало цикла
i = 0  # итерация
num_of_student = 1  # номер студента
doc_for_student = canvas.Canvas(students_name + ".pdf")
doc_for_student.setFont("Arial", 12)
doc_for_student.drawString(500, top, date.today().strftime("%d.%m.%Y"))
doc_for_student.drawString(center, top, subject)
doc_for_student.drawString(center, top - interval * (i+1), "Вариант " + str(i + 1))  # для студента
doc_for_student.drawString(start, top - interval * (i+2), "Тема")
doc_for_student.drawString(start, top - interval * (i+3), str(i+1) + ". Задание")

doc_for_teacher.drawString(center, top - num_of_student * interval * (i+1), "Вариант " + str(i + 1))  # для преподавателя
doc_for_teacher.drawString(start, top - num_of_student * interval * (i+2), "Ответ")  # для преподавателя
# конец цикла

doc_for_teacher.save()  # Сохраняем PDF файл
doc_for_student.save()