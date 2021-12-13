from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import re
import hashlib

app = Flask(__name__)

app.secret_key = 'secret key'

#password = os.getenv('MYSQL_PASSWORD')     --auto gets password need to fix
mysql = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "",
  database="setstats"
)


@app.route('/')
def index():
    return checkLoginOrRedirect('index.html')


@app.route('/deadlift/')
def deadlift():
    return checkLoginOrRedirect('deadlift.html')


@app.route('/graph/')
def squad():
    return checkLoginOrRedirect('graph.html')

@app.route('/sessions/<id>')
def sessionselection(id):
    cursor = mysql.cursor(dictionary=True)
    cursor.execute('SELECT * FROM session WHERE session_id = ' + str(id))
    lift = cursor.fetchone()
    # If account exists in trainee table in  database
    if lift:
        # Create session data
        lift['id'] = lift['session_id']
        lift['best_xy'] = lift['best_xy']
        lift['worst_xy'] = lift['worst_xy']
        lift['time'] = lift['time']
        lift['rep_num'] = lift['rep_num']
        lift['set_num'] = lift['set_num']

        return redirect("/")

    return checkLoginOrRedirect('history.html')


@app.route('/sessions/')
def history():
    if not loggedIn():
        return redirect("/")

    cursor = mysql.cursor(dictionary=True)
    traineeid = session['trainee_id']
    cursor.execute('SELECT * FROM history WHERE trainee_id = ' + str(traineeid))
    data = cursor.fetchall()

    return checkLoginOrRedirectWithData('session_selection.html', data)

@app.route('/<path:dummy>')
def fallback(dummy=None):
    return redirect("/")

def loggedIn():
    if session.get('loggedin') is None or (session.get('loggedin') == False):
        return False
    return True

def checkLoginOrRedirect(template):
    if session.get('loggedin') is None or (session.get('loggedin') == False):
        return redirect("/login")
    return render_template(template)


def checkLoginOrRedirectWithData(template, data):
    if session.get('loggedin') is None or (session.get('loggedin') == False):
        return redirect("/login")
    return render_template(template, data = data)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message
    msg = ''


    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        cursor = mysql.cursor(dictionary=True)
        cursor.execute('SELECT * FROM trainee WHERE username = %s AND password = %s', (username, password,))
        # Fetch  record and return result
        trainee = cursor.fetchone()
        # If account exists in trainee table in  database
        if trainee:
            # Create session data
            session['loggedin'] = True
            session['trainee_id'] = trainee['trainee_id']
            session['username'] = trainee['username']

            return redirect("/")
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
        hash_pass = hashlib.md5(password.encode("utf-8")).hexdigest()
        # Check if account exists using MySQL
        cursor = mysql.cursor(dictionary=True)
        cursor.execute('SELECT * FROM trainee WHERE username = %s', ([username]))
        exists = cursor.fetchone()
        if exists:
            msg = 'Account already exists!'

        else:
            if re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$", password):
                # Account doesnt exists and the form data is valid, now insert new account into trainee table
                cursor.execute('INSERT INTO trainee (username, password) VALUES (%s, %s)', ([username], [hash_pass]))
                mysql.connection.commit()
                msg = 'You have successfully registered!'
                return render_template('index.html')
            msg = 'Password needs to have minimum six characters, at least one letter and one number'

    return render_template('register.html', msg=msg)


@app.route('/trainerLogin/', methods=['GET', 'POST'])
def trainerLogin():
    # Output message
    msg = ''


    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        cursor = mysql.cursor(dictionary=True)
        cursor.execute('SELECT * FROM trainer WHERE username = %s AND password = %s', (username, password,))
        # Fetch  record and return result
        trainer = cursor.fetchone()
        # If account exists in trainer table in  database
        if trainer:
            # Create session data
            session['loggedin'] = True
            session['trainer_id'] = trainer['trainer_id']
            session['username'] = trainer['username']

            return redirect("/")
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

    return render_template('trainerLogin.html', msg=msg)

@app.route('/trainerRegister/', methods=['GET', 'POST'])
def trainerRegister():
    # Output message if something goes wrong...
    msg = ''

    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.cursor(dictionary=True)
        cursor.execute('SELECT * FROM trainer WHERE username = %s', ([username]))
        exists = cursor.fetchone()
        if exists:
            msg = 'Account already exists!'

        else:
            if re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$", password):
                # Account doesnt exists and the form data is valid, now insert new account into trainer table
                cursor.execute('INSERT INTO trainer (username, password, email) VALUES (%s, %s, %s)', ([username], [password],[email]))
                mysql.connection.commit()
                msg = 'You have successfully registered!'
                return render_template('index.html')
            msg = 'Password needs to have minimum six characters, at least one letter and one number'

    return render_template('trainerRegister.html', msg=msg)


@app.route('/logout')
def logout():

    session.pop('loggedin', None)
    session.pop('trainee_id', None)
    session.pop('username', None)


    return redirect(url_for('login'))
app.run(debug=True)
