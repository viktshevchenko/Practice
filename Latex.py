# -*- coding: utf-8 -*-
from datetime import date
from pylatex import Document, Package, Section, Command # pip install pylatex (cmd)

current_day = date.today()  # сегодняшняя дата
subject = ""  # название предмета
students_name = "ФИО"  # запрос из бд

doc_for_teacher = Document("Ответы")  # создание документа с названием "Ответы"
doc_for_teacher.packages.add(Package('babel', options=['rissian']))  # устанавливаем запись в файл кириллицей
doc_for_teacher.append(subject)  # записываем в файл название предмета
doc_for_teacher.append(current_day)  # записываем в файл дату создания кр

# начало цикла генерации заданий для студента и ответов для преподавателя
variant = 1  # номер варианта
num_task = 1  # номер задания
task = ""  # задание
answer = ""

doc_for_student = Document(students_name)  # создание документа с названием имени студента
doc_for_student.packages.add(Package('babel', options=['rissian']))  # устанавливаем запись в файл кириллицей
doc_for_student.append(subject)  # записываем в файл название предмета
doc_for_student.append(current_day)  # записываем в файл дату создания кр
doc_for_student.append(variant)  # записываем в файл номер варианта
doc_for_student.append(variant)  # записываем в файл название темы
doc_for_student.append(str(num_task) + ". " + task)  # записываем в файл задание

doc_for_teacher.append(variant)  # записываем в файл ответов номер варианта
doc_for_teacher.append(str(num_task) + ". " + answer)  # записываем в файл ответ

doc_for_student.generate_pdf(students_name, clean_tex=False)  # создаем pdf для студента
# конец цикла

doc_for_teacher.generate_pdf("Ответы", clean_tex=False)  # создаем pdf для преподавателя