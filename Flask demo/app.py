from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the basic Flask App"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/user/<name>')
def greet(name):
    return render_template("index.html",name=name)

@app.route("/courses")
def for_loop():
    list_of_courses = ['Java', 'Python', 'C++', 'MATLAB']
    return render_template("courses.html", courses=list_of_courses)

if __name__ == '__main__':
    app.run(debug=True)

