from flask import Flask, render_template
import pymysql.cursors

app = Flask(__name__)
student = ''
print (student)

connection = pymysql.connect(host='mrbartucz.com',
                             user='sq8822nj',
                             password='Whyskar|3301',
                             db='sq8822nj_Assignment_Two',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELECT First_Name from Students"
        cursor.execute(sql)

        for result in cursor:
            student = result
finally:
        connection.close()
        
print (student)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name = name)

@app.route ('/default')
def default():
    return 'hi'

@app.route ('/students')
def students():
    return (student) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')