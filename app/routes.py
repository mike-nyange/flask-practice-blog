from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm, RegistrationForm
from app.models import User, Post
from app import app

posts = [
    {
        'author':'Mike Mwanyika',
        'title':'First Blog Post',
        'content':'Ile ya wazii',
        'date_posted':'July 5, 2022'
    },
    {
        'author':'Mike Mwanyika',
        'title':'First Blog Post',
        'content':'Ile ya wazii',
        'date_posted':'July 5, 2022'
    },
    {
        'author':'Mike Mwanyika',
        'title':'First Blog Post',
        'content':'Ile ya wazii',
        'date_posted':'July 5, 2022'
    },
]

@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET' ,'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
        
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET' ,'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login for {form.email.data} is successful', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title="Login", form=form)