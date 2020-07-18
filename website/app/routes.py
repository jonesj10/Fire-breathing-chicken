from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)



@app.route('/')
def default():
    return render_template('base.html', title='Hello')



@app.route('/index')
def index():
    return render_template('index.html', title='INDEX')


@app.route('/nav')
def nav():
    return render_template('nav.html', title='Hello')


@app.route('/interactive')
def interactive():
	return render_template('interactive.html')


@app.route('/snake')
def snake():
    return render_template('snake.html')

#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")



@app.route('/table')
def table():
    with open("/home/jones/Documents/firebreathingchicken/fire-breathing-chicken/website/app/location.txt", "r") as f:

        
        content = f.read()
        print(content)
    return content 
