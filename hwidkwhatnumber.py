#я решила написать все заново с нуля сама, кроме первых двух функций!

from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)



@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/thanks', methods=['POST'])
def save_to_csv():
    if request.method == 'POST':
        correct = request.form['haveuheard']
        andnow = request.form['woulduse']
        gender = request.form['gender']
        age = request.form['age']
        name = request.form['name']
        surname = request.form['surname']
        fin_form = 'Спасибо за ваш ответ!'
        fieldnames = ['haveuheard', 'woulduse','gender', 'age', 'name', 'surname']
        with open('resultatiki.csv', 'a+', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'haveuheard': correct, 'woulduse': andnow, 'age': age , 'gender': gender,
                             'name': name, 'surname': surname})
        return render_template("thanks.html", fin_form=fin_form)


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/stats', methods=['GET'])
def stats():
    yes1 = []
    no1 = []
    yes2 = []
    no2 = []
    with open ('resultatiki.csv', 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(',')
            if line[0] == 'yes':
                yes1.append(line[0])
            else:
                no1.append(line[0])
            if line[1] == 'yes':
                yes2.append(line[1])
            else:
                no2.append(line[1])
        a = 'Слышали: %s' % (len(yes1))
        b = 'Не слышали: %s'% (len(no1))
        c = 'Употребляют в речи: %s'%(len(yes2))
        d = 'Не употребляют в речи: %s'% (len(no2))
        stats = a + '\n' + b + '\n' + c + '\n' + d
    return render_template("stats.html", stats=stats)
        
    
    

@app.route('/result', methods=['POST'])
def get_res():
    what = request.form['what_search']
    with open ('resultatiki.csv', 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if what in line:
                result = line
    return render_template("result.html", result=result)

##@app.route('/json')
##csv_dict = {}
##def json_maker:
##    with open('results1.csv', 'r+', encoding='utf-8') as csvfile:
##        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
##        for row in reader:
##            name = row['name'] + row


if __name__ == '__main__':
    app.run(debug=True)
