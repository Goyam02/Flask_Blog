from flask import Flask, render_template
app = Flask(__name__)


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

if __name__ == "__main__":
    app.run()