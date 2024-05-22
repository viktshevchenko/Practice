import psycopg2

from funcs_for_file_querry import *



try:
    conn = psycopg2.connect(dbname='practice', user='postgres', password='12345', host='localhost')
    conn.autocommit = True

    arr0 = ['3', '4']
    arr = [arr0[0], arr0[1]]
    group ='ИТПМ-123'
    tasks_and_answers = []
    answers = []
    variant = []
    bool_f = [1, 2]
    sknf_sdnf_f = [1, 2]

    with conn.cursor() as cursor:
        querry = "select text from templates where name = %s"
        name_sknf = 'Построение СКНФ'
        name_sdnf = 'Построение СДНФ'
        cursor.execute(querry, (name_sknf,))
        task_tuple = cursor.fetchone()
        task = ', '.join(task_tuple)
        task = task[:-1] + str(sknf_sdnf_f[1]) + task[-1:]
        func_bool = eval(task)
        variant.append(func_bool)
        cursor.execute(querry, (name_sdnf,))
        task_tuple = cursor.fetchone()
        task = ', '.join(task_tuple)
        task = task[:-1] + str(sknf_sdnf_f[1]) + task[-1:]
        func_bool = eval(task)
        variant.append(func_bool)
    print(variant)







except Exception as _ex:
    print('Can`t establish connection to database', _ex)
    traceback.print_exc()
finally:
    if conn:
        conn.close()
        print("Connection over")