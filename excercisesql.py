import sqlite3

# подключаемся к базе данных
conn = sqlite3.connect('nanaivowels.db')

# создаем объект "курсор", которому будем передавать запросы
c = conn.cursor()

# создаем таблицу
c.execute("CREATE TABLE IF NOT EXISTS nanaivowels(dictor text, sex text, village text, sound text, f1 float, f2 float)")

# вставляем строку
with open ('nanai-vowels.csv', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(';')
        a = line[0]
        b = line[1]
        d = line[2]
        e = line[3]
        f = line[4]
        g = line[5]
        c.execute("INSERT INTO nanaivowels VALUES (?, ?, ?, ?, ?, ?)", (a, b, d, e, f, g))


c.execute('SELECT * FROM nanaivowels ORDER BY sex')
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
# сохраняем изменения
conn.commit()

# отключаемся от БД
conn.close()
