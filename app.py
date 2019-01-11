from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'online_cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:cook1book2@ds129914.mlab.com:29914/online_cookbook'

mongo = PyMongo(app)

@app.route('/')

@app.route('/home')
def home():
    """
    Return index.html which is the first page the user will see
    """
    return render_template("index.html")
    
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Direct user to signin page where they can enter their username
    and password and manage their recipes
    """
    if 'username' in session:
        return render_template('index.html',
                                message="You are already signed in!")
    
    if request.method == 'POST':
        users = mongo.db.users
        user_signin = users.find_one({'username': request.form['username']})

        if user_signin:
            if request.form['password'] == user_signin['password']:
                session['username'] = request.form['username']
                return redirect(url_for('home'))
        return render_template('signin.html', message='Invalid username or password')
    return render_template('signin.html', message='')
    
@app.route('/signout')
def signout():
    """
    Sign user out of the session
    """
    if 'username' in session:
        session.pop('username')
        return render_template('message.html',
                               message='Signed out. See you later!')
    return render_template('message.html',
                           message='You have already signed out!')
                           
@app.route('/register')
def register():
    """
    Register new user into the database
    """
    if 'username' in session:
        return render_template('register.html', message='You are already signed in and registered')

    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if request.form['username'] and request.form['password']:
            # Check for existing user to avoid re-registering the same user
            if existing_user is None:
                password = request.form['password']
                users.insert({'username': request.form['username'], 'password': password})
                session['username'] = request.form['username']
                return redirect(url_for('home'))
            return render_template('register.html',
                                   message='Username ' + str(existing_user['username']) + ' already exists')

        return render_template('register.html',
                                message='Enter a username and password')

    return render_template('register.html', message='')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)