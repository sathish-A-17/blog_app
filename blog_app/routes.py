from flask import render_template, url_for, flash, redirect
from blog_app import app
from blog_app.forms import RegistrationForm, LoginForm
from blog_app.models import User,Post

posts = [{
    'author': 'Jane',
    'title': 'Blog Post 1',
    'content': 'First blog post',
    'date_posted': 'feb 21,2024'
},
    {
        'author': 'James',
        'title': 'Blog Post 2',
        'content': 'Second blog post',
        'date_posted': 'feb 27,2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check Email and Password', 'danger')
    return render_template('login.html', title='Login', form=form)
