import psycopg2
import random
try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='project', user='postgres', password='12345', host='localhost')
    conn.autocommit = True
    #заносим в бд шаблоны из файла 
    #дубикаты удаляются
    with open(r'C:\Users\angel\OneDrive\Desktop\templates.txt','r') as templates_file:
        for line in templates_file:
            with conn.cursor() as cursor:
                line = (line, )
                cursor.execute(
                    """insert into templates(template)
                    values(%s)""",(line)
                )
    with conn.cursor() as cursor:
        cursor.execute(
            """delete from templates where (template) in (
            select template from templates group by template having count(*) > 1
            )"""
        )
        #делаем задание расставляем переменные на места и заносим в бд, дубикаты удаляются
    with open(r'C:\Users\angel\OneDrive\Desktop\templates.txt','r') as templates_file:
        for line in templates_file:
            line2 = ''
            variables = 'abcd'
            max = 3
            for i in line:
                if i == 'x':
                    variable = random.randint(0, max)
                    line2 += variables[variable]
                else:
                    line2 += i
            with open(r"C:\Users\angel\OneDrive\Desktop\tasks.txt", 'w') as tasks_file:
                tasks_file.write(line2)
            line2 = (line2, )
    
            with conn.cursor() as cursor:
                cursor.execute(
                    """insert into tasks(task) values(%s);""", line2
                )
            with conn.cursor() as cursor:
                cursor.execute(
                    """delete from tasks where (task) in (
                    select task from tasks group by task having count(*) > 1
                    )"""
                )
                #разобоаться с темами
            

        
        


            






except Exception as _ex:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database', _ex)
finally:
    if conn:
        conn.close()
        print("Connection over")
