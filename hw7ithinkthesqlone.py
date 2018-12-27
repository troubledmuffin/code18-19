from flask import Flask, render_template, request
import csv
import json
import sqlite3

app = Flask(__name__)




# подключаемся к базе данных
conn = sqlite3.connect('gazety.db')

# создаем объект "курсор", которому будем передавать запросы
c = conn.cursor()

# создаем таблицу
c.execute("CREATE TABLE IF NOT EXISTS gazety(name text, text text, url text)")

# вставляем строку
with open ('gazety.csv', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(';')
        a = line[0]
        b = line[1]
        d = line[2]
        c.execute("INSERT INTO gazety VALUES (?, ?, ?)", (a, b, d))

# сохраняем изменения
conn.commit()

# отключаемся от БД
conn.close()

@app.route('/', methods=['POST'])
def get_res():
    what = request.form['what_search']
    with open ('gazety.csv', 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if what in line:
                result = line
    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
