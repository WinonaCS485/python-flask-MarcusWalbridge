from flask import Flask, render_template
import pymysql.cursors

app = Flask(__name__)

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
    try:
        with connection.cursor() as cursor:
            # Select all Students
            sql = "SELECT * from Students"
        
            # execute the SQL command
            cursor.execute(sql)
        
            # get the results
            for result in cursor:
                print (result)

    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
