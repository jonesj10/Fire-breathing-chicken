from flask import Flask
from flask import render_template
from app.forms import LoginForm

app = Flask(__name__)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)