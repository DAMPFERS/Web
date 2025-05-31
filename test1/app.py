from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Конфигурация MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'yourdatabase'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Проверка логина и пароля в базе данных
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        if user:
            return "Hello, World!"
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)