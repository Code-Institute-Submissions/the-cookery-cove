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
    Return home.html which is the first page the user will see
    """
    return render_template("home.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)