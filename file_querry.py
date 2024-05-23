import psycopg2
import traceback
import random
import pylatex
import chardet
from reportlab.pdfgen import canvas  # pip install reportlab
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime
from funcs_for_file_querry import *
from datetime import date

center = 230
start = 100
top = 790
interval = 22

pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))  # Загружаем шрифт с поддержкой кириллицы
try:
    
    conn = psycopg2.connect(dbname='practice', user='postgres', password='12345', host='localhost')
    conn.autocommit = True
    

    with open('info.txt', 'r') as info_file:
        info_file = info_file.read()
        info_file = info_file.split()
        flag = 0
        amount_tasks = 0
        if 'Преподаватель' in info_file:
            flag = 1
            subject = info_file[0] + ' ' + info_file[1]
            group = info_file[3]
            bool_f = [info_file[4], info_file[5]] # первое число кол-во заданий, второк кол-во переменных
            sknf_sdnf_f = [info_file[6], info_file[7]]
            zegalkin_f = [info_file[8], info_file[9]]

            with conn.cursor() as cursor:
                querry = "select count (*) from students where id_group = (select id from band where name = %s)"
                cursor.execute(querry, (group,))
                num_tuple = cursor.fetchone()
                num_stundents = num_tuple[0]

            amount_tasks = int(bool_f[0]) + int(sknf_sdnf_f[0]) + int(zegalkin_f[0])  # кол-во заданий в варианте
        else:
            subject = info_file[0] + ' '+ info_file[1]
            name = info_file[2] + ' ' + info_file[3] + ' ' + info_file[4]

            student_name = name

            bool_f = [info_file[5], info_file[6]] 
            sknf_sdnf_f = [info_file[7], info_file[8]]
            zegalkin_f = [info_file[9], info_file[10]]

            amount_tasks = int(bool_f[0]) + int(sknf_sdnf_f[0]) + int(zegalkin_f[0]) #кол-во заданий в варианте
        
    if flag == 0:

        variant = []
        tasks_and_answers = []
        answers = []
        id_template_list = []
        with conn.cursor() as cursor:
            querry = "select id from students where name = %s"
            cursor.execute(querry, (name,))
            id_student_tuple = cursor.fetchone()
            id_student = id_student_tuple[0]

        bool_f_first_iter = True

        for i in range(int(bool_f[0])):
            if bool_f_first_iter == True:
                variant.append('Способы задания булевых функций')
                bool_f_first_iter == False
                with conn.cursor() as cursor:
                    querry = "select id from templates where name = %s"
                    name = 'Способы задания булевых функций'
                    cursor.execute(querry, (name,))
                    id_template_tuple = cursor.fetchone()
                    id_template = id_template_tuple[0]
                    id_template_list.append(id_template)

            with conn.cursor() as cursor:
                querry = "select text, id from templates where name = %s"
                name = 'Способы задания булевых функций'
                cursor.execute(querry, (name,))
                task_tuple = cursor.fetchall()
                task = task_tuple[0][0]
                #id_template_list.append(task_tuple[0][1])
                task = task[:-1] + bool_f[1] + task[-1:]
                func_bool = eval(task)
                variant.append(func_bool)
                answers.append(truth_table(func_bool, int(bool_f[1])))

        zegalkin_first_iter = True

        for i in range(int(zegalkin_f[0])):
            if zegalkin_first_iter == True:
                variant.append('Построение полинома Жегалкина')
                zegalkin_first_iter = False
            with conn.cursor() as cursor:
                querry = "select text, id from templates where name = %s"
                name = 'Построение полинома Жегалкина'
                cursor.execute(querry, (name,))
                task_tuple = cursor.fetchall()
                task = task_tuple[0][0]
                id_template_list.append(task_tuple[0][1])
                task = task[:-1] + zegalkin_f[1] + task[-1:]
                func_bool = eval(task)
                variant.append(func_bool)
                answers.append(polinom_Zhegalkina(func_bool, int(zegalkin_f[1])))

        sknf_sdnf_first_iter = True

        for i in range(int(sknf_sdnf_f[0])):
            if sknf_sdnf_first_iter == True:
                variant.append('Построение СКНФ и СДНФ')
            with conn.cursor() as cursor:
                querry = "select text, id from templates where name = %s"
                name_sknf = 'Построение СКНФ'
                name_sdnf = 'Построение СДНФ'
                cursor.execute(querry, (name_sknf,))
                task_tuple = cursor.fetchall()
                task = task_tuple[0][0]
                id_template_list.append(task_tuple[0][1])

                task = task[:-1] + sknf_sdnf_f[1] + task[-1:]
                func_bool = eval(task)
                variant.append(func_bool)

                answers.append(sknf(func_bool, int(sknf_sdnf_f[1])))

                cursor.execute(querry, (name_sdnf,))
                task_tuple = cursor.fetchall()


                task = task_tuple[0][0]
                id_template_list.append(task_tuple[0][1])

                task = task[:-1] + sknf_sdnf_f[1] + task[-1:]
                func_bool = eval(task)
                variant.append(func_bool)
                answers.append(sdnf(func_bool, int(sknf_sdnf_f[1])))

        variant = ','.join(map(str, variant))
        answers = ','.join(map(str, answers))
        variant_list = variant.split(',')
        answers_list = answers.split(',')


        with conn.cursor() as cursor:
            querry = "insert into variants (id_template, text, answers, num) values (%s, %s, %s, %s) returning id"

            cursor.execute(querry, (id_template_list, variant, answers, amount_tasks))

            id_var_tuple = cursor.fetchall()
            id_var = id_var_tuple[0][0]
            querry2 = "insert into student_var(id_student, id_var, data) values (%s, %s, %s) returning id"
            event_date = datetime.now()
            cursor.execute(querry2, (id_student, id_var, event_date))
            id_stud_var_tuple = cursor.fetchall()
            id_stud_var = id_stud_var_tuple[0][0]
            i = 0
            while i < len(tasks_and_answers):
                querry3 = "insert into tasks (id_stud_var, text_task, text_ans) values (%s, %s, %s)"
                cursor.execute(querry3, (id_stud_var, tasks_and_answers[i], tasks_and_answers[i+1]))
                i += 2
        k3 = 1
        doc_for_one_student = canvas.Canvas(student_name + ' вариант.pdf')
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))  # Загружаем шрифт с поддержкой кириллицы
        doc_for_one_student.setFont("Arial", 12)  # Устанавливаем текущий шрифт

        doc_for_one_student.drawString(500, 790, date.today().strftime("%d.%m.%Y"))  # Добавляем дату
        k3 += 1
        doc_for_one_student.drawString(center, 790, subject)  # Добавляем название предмета
        k3 += 1



        for i in variant_list:
            doc_for_one_student.drawString(start, top - interval * k3, i)
            k3 += 1
        doc_for_one_student.save()





        k4 = 1
        doc_for_one_student_answers = canvas.Canvas(student_name + ' ответы.pdf')
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))  # Загружаем шрифт с поддержкой кириллицы
        doc_for_one_student_answers.setFont("Arial", 12)  # Устанавливаем текущий шрифт
        doc_for_one_student_answers.drawString(500, 790, date.today().strftime("%d.%m.%Y"))  # Добавляем дату
        k4 += 1
        doc_for_one_student_answers.drawString(center, 790, subject)  # Добавляем название предмета
        k4 += 1




        for j in answers_list:
            doc_for_one_student_answers.drawString(start, top - interval * k4, j)
            k4 += 1
        doc_for_one_student_answers.save()



    #для всей группы


    else:
        answers_all_group = []


        k2 = 1
        doc_for_teacher = canvas.Canvas("Ответы.pdf")  # Создаем новый PDF файл

        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))  # Загружаем шрифт с поддержкой кириллицы

        doc_for_teacher.setFont("Arial", 12)  # Устанавливаем текущий шрифт

        doc_for_teacher.drawString(500, 790, date.today().strftime("%d.%m.%Y"))  # Добавляем дату

        doc_for_teacher.drawString(center, 790, subject)  # Добавляем название предмета
        k2 += 1






        number_variant = 1
        with conn.cursor() as cursor:

            querry = "select id from students where id_group = (select id from band where name = %s)"
            name = group
            cursor.execute(querry, (name,))
            id_student_tuple = cursor.fetchall()
        id_student_list = [t[0] for t in id_student_tuple]
        id_student_list_index = 0

        for student in range(num_stundents):






            variant = []
            templates_list = []
            answers = []

            tasks_and_answers = [] #первое - задание, после него ответ, так до конца


            with conn.cursor() as cursor:
                querry = "select name from students where id_group = (select id from band where name = %s) and id = %s"
                name_group = (group,)
                cursor.execute(querry, (name_group[0], id_student_list[id_student_list_index]))
                student_name = cursor.fetchone()
            variant.append(student_name[0])
            #id_student_list_index += 1




            first_inter_bool_f = True
            for i in range(int(bool_f[0])):
                if first_inter_bool_f == True:
                    variant.append('Способы задания булевых функций')
                    answers.append('Способы задания булевых функций')

                    with conn.cursor() as cursor:
                        querry = "select id from templates where name = %s"
                        name = 'Способы задания булевых функций'
                        cursor.execute(querry, (name,))
                        id_template_tuple = cursor.fetchall()
                        id_template = id_template_tuple[0]
                        templates_list.append(id_template)

                    first_inter_bool_f = False




                with conn.cursor() as cursor:
                    querry = "select text, id from templates where name = %s"
                    name = 'Способы задания булевых функций'
                    cursor.execute(querry, (name,))
                    task_id_tuple = cursor.fetchall()#первый элемент функция, второй id
                    task = task_id_tuple[0][0]
                    id_tem_bool_f = task_id_tuple[0][1]
                    task = task[:-1] + bool_f[1] + task[-1:]
                    func_bool = eval(task)
                    variant.append(func_bool)
                    #генерация ответа
                    count_var = int(bool_f[1])
                    ans = truth_table(func_bool, count_var)
                    answers.append(ans)
                    tasks_and_answers.append(func_bool)
                    tasks_and_answers.append((ans))

            first_inter_zegalkin_f = True
            for i in range(int(zegalkin_f[0])):
                if first_inter_zegalkin_f == True:

                    variant.append('Построение полинома Жегалкина')
                    answers.append('Построение полинома Жегалкина')


                    with conn.cursor() as cursor:
                        querry = "select id from templates where name = %s"
                        name = 'Построение полинома Жегалкина'
                        cursor.execute(querry, (name,))
                        id_template_tuple = cursor.fetchall()
                        id_template = id_template_tuple[0]
                        templates_list.append(id_template)


                    first_inter_zegalkin_f = False
                with conn.cursor() as cursor:
                    querry = "select text, id from templates where name = %s"
                    name = 'Построение полинома Жегалкина'
                    cursor.execute(querry, (name,))
                    task_id_tuple = cursor.fetchall()
                    task = task_id_tuple[0][0]
                    id_tem_zegalkin_f = task_id_tuple[0][1]
                    task = task[:-1] + zegalkin_f[1] + task[-1:]
                    func_bool = eval(task)
                    variant.append(func_bool)
                    count_var = int(zegalkin_f[1])
                    ans = polinom_Zhegalkina(func_bool, count_var)
                    answers.append(ans)
                    tasks_and_answers.append(func_bool)
                    tasks_and_answers.append((ans))



            first_inter_sknf_sdnf_f = True
            for i in range(int(sknf_sdnf_f[0])):
                if first_inter_sknf_sdnf_f == True:

                    variant.append('Построение СКНФ и Построение СДНФ')
                    answers.append('Построение СКНФ и Построение СДНФ')
                    with conn.cursor() as cursor:
                        querry = "select id from templates where name = %s"
                        name = 'Построение СКНФ'
                        cursor.execute(querry, (name,))
                        id_template_tuple = cursor.fetchall()
                        id_template = id_template_tuple[0]
                        templates_list.append(id_template)
                    with conn.cursor() as cursor:
                        querry = "select id from templates where name = %s"
                        name = 'Построение СДНФ'
                        cursor.execute(querry, (name,))
                        id_template_tuple = cursor.fetchall()
                        id_template = id_template_tuple[0]
                        templates_list.append(id_template)

                    first_inter_sknf_sdnf_f = False


                with conn.cursor() as cursor:
                    querry = "select text, id from templates where name = %s"
                    name_sknf = 'Построение СКНФ'
                    name_sdnf = 'Построение СДНФ'
                    cursor.execute(querry, (name_sknf,))
                    task_id_tuple = cursor.fetchall()
                    task = task_id_tuple[0][0]
                    id_tem_sknf = task_id_tuple[0][1]
                    task = task[:-1] + str(sknf_sdnf_f[1]) + task[-1:]
                    func_bool = eval(task)
                    variant.append(func_bool)
                    count_var = int(sknf_sdnf_f[1])
                    ans = sknf(func_bool, count_var)
                    answers.append(ans)

                    tasks_and_answers.append(func_bool)
                    tasks_and_answers.append(ans)

                    cursor.execute(querry, (name_sdnf,))
                    task_id_tuple = cursor.fetchall()
                    task = task_id_tuple[0][0]
                    id_tem_sdnf = task_id_tuple[0][1]
                    task = task[:-1] + str(sknf_sdnf_f[1]) + task[-1:]
                    func_bool = eval(task)
                    variant.append(func_bool)
                    count_var = int(sknf_sdnf_f[1])
                    ans = sdnf(func_bool, count_var)
                    answers.append(ans)

                    tasks_and_answers.append(func_bool)
                    tasks_and_answers.append(ans)

            variant = ','.join(map(str, variant))
            answers = ','.join(map(str, answers))
            variant_list = variant.split(',')
            answers_list = answers.split(',')
            #print(variant_list)
            #print(answers_list)

            k = 1

            doc_for_student = canvas.Canvas(student_name[0] + ".pdf")
            doc_for_student.setFont("Arial", 12)
            doc_for_student.drawString(500, top, date.today().strftime("%d.%m.%Y"))
            doc_for_student.drawString(center, top, subject)
            doc_for_student.drawString(center, top - interval *  k, "Вариант " + str(number_variant))
            k += 1
            doc_for_student.drawString(start, top - interval  * k, "Задания:")
            k += 1


            k2 += 1

            line_count = 1



           # first_iter_pdf = True
            for i in variant_list:

                doc_for_student.drawString(start, top - interval * k, i)
                k += 1


            for j in answers_list:


                #doc_for_teacher.drawString(start, top - interval)
                doc_for_teacher.drawString(start, top - interval * k2, j)
                k2 += 1
                if k2 > 28:
                    doc_for_teacher.showPage()
                    doc_for_teacher.setFont("Arial", 12)  # Устанавливаем текущий шрифт
                    k2 = 1


            number_variant += 1
            doc_for_student.save()







            with conn.cursor() as cursor:

                querry = "insert into variants (id_template, text, answers, num) values (%s, %s, %s, %s) returning id"

                cursor.execute(querry, (templates_list, variant, answers , amount_tasks))

                new_var_id = cursor.fetchone()[0]


            with conn.cursor() as cursor:
                querry = "insert into student_var (id_student, id_var, data) values (%s, %s, %s) RETURNING id"
                event_date = datetime.now()
                cursor.execute(querry, (id_student_list[id_student_list_index], new_var_id, event_date))
                id_stud_var_tuple = cursor.fetchall()
                id_stud_var_int = id_stud_var_tuple[0]

            i = 0
            while i < len(tasks_and_answers):
                with conn.cursor() as cursor:
                    querry = "insert into tasks (id_stud_var, text_task, text_ans) values (%s, %s, %s)"
                    cursor.execute(querry, (id_stud_var_int, tasks_and_answers[i], tasks_and_answers[i + 1]))
                    i += 2










            id_student_list_index += 1
        doc_for_teacher.save()






#ФИО, тема добавить в txt




















except Exception as _ex:
    print('Can`t establish connection to database', _ex)
    traceback.print_exc()
finally:
    if conn:
        conn.close()
        print("Connection over")

