import psycopg2

try:

    conn = psycopg2.connect(dbname='practice', user='postgres', password='12345', host='localhost')
    conn.autocommit = True
    
    with conn.cursor() as cursor:

        cursor.execute("insert into cates (name) values('Математический анализ')")
        cursor.execute("insert into cates (name) values('Дискретная математика')")
        
        cursor.execute("insert into templates (name, text, id_cat) values\
                       ('Способы задания булевых функций', 'generate_function()', (select id from cates where name = 'Дискретная математика')),\
                       ('Построение полинома Жегалкина', 'generate_function()', (select id from cates where name = 'Дискретная математика')),\
                       ('Построение СКНФ', 'generate_function()', (select id from cates where name = 'Дискретная математика')), \
                       ('Построение СДНФ', 'generate_function()', (select id from cates where name = 'Дискретная математика'))")

        

        cursor.execute("insert into band(name) values ('ИТПМ-123')")

        cursor.execute("insert into students (name, id_group) values \
                       ('Ангелов Владимир Михайлович', (select id from band where name = 'ИТПМ-123')),\
                       ('Водорезова Кристина Олеговна', (select id from band where name = 'ИТПМ-123')),\
                       ('Прибытков Степан Евгеньевич', (select id from band where name = 'ИТПМ-123')),\
                       ('Бирюкова Виктория Кто-то-там', (select id from band where name = 'ИТПМ-123'))")











except Exception as _ex:
    print('Can`t establish connection to database', _ex)
finally:
    if conn:
        conn.close()
        print("Connection over")
