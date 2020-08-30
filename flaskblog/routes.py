from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
	{
		'author': 'George Carey',
		'title': 'My First Blog',
		'content': 'First post',
		'date_posted': '28 July 2020'

	},
	{
		'author': 'George Carey',
		'title': 'And another one',
		'content': 'Second post',
		'date_posted': '28 July 2020'
	}
]

# route information
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)  

@app.route('/about')
def about():
	return render_template("about.html", title='About Us')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "admin@blog.com" and form.password.data == "password":
			flash("You have been logged in!", "success")
			return redirect(url_for("home"))
		else:
			flash("Login Unsuccessful. Please check username and password", "danger")
	return render_template('login.html', title='Login', form=form)