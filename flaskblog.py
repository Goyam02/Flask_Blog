from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '0f2ce7baaad8e79bba4abb62835d9e62'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpeg')
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

posts = [
    {
        'author' : 'Goyam Jain',
        'title' : 'Blog Post'   , 
        'content' : 'First Post Content',
        'date_posted' : 'Jan 15,2025'
    },
    {
        'author' : ' Jain Goyam',
        'title' : 'Blog Post'   , 
        'content' : 'Second Post Content',
        'date_posted' : 'Jan 15,2025'
    }

]




@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html" , posts = posts)

@app.route("/about")
def about():
    return render_template("about.html", title = "About" )

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)

if __name__ == "__main__":
    app.run(debug=True)