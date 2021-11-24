from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'setstats'

# Intialize MySQL
mysql = MySQL(app)
@app.route('/')
def index():
    if session.get('loggedin') is None or (session.get('loggedin') == False):
            return redirect("/login")
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM trainee WHERE username = %s AND password = %s', (username, password,))
        # Fetch  record and return result
        trainee = cursor.fetchone()
        # If account exists in trainee table in  database
        if trainee:
            # Create session data
            session['loggedin'] = True
            session['trainee_id'] = trainee['trainee_id']
            session['username'] = trainee['username']

            return render_template("index.html")
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

    return render_template('login.html', msg=msg)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''

    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM trainee WHERE username = %s', ([username]))
        exists = cursor.fetchone()
        if exists:
            msg = 'Account already exists!'
        # TODO - Security: Regex expressions

        # Account doesnt exists and the form data is valid, now insert new account into accounts table
        cursor.execute('INSERT INTO trainee (username, password) VALUES (%s, %s)', ([username], [password]))
        mysql.connection.commit()
        msg = 'You have successfully registered!'

    return render_template('register.html', msg=msg)
app.run(debug=True)