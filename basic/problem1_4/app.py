# 1. Create a Flask app that displays "Hello, World!" on the homepage.
from flask import Flask, render_template, request, session

app=Flask(__name__)

#showing index page
@app.route('/')
def index_page():
    return render_template('index.html')

# 1. Create a Flask app that displays "Hello, World!" on the homepage.
@app.route('/helloworld')
def hell_world():
    return "Hello, World!"

# 2. Build a Flask app with static HTML pages and navigate between them.
@app.route('/about')
def show_about():
    return render_template('about.html')

@app.route('/contact')
def show_contact():
    return render_template('contact.html')

@app.route('/services')
def show_services():
    return render_template('service.html')

# 3. Develop a Flask app that uses URL parameters to display dynamic content.
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

# 4. Create a Flask app with a form that accepts user input and displays it.
@app.route('/showdetails',methods=['GET','POST'])
def show_details():
    name=request.form.get('name')
    roll_no=request.form.get('roll')
    return f"Name : {name}\nRoll No. : {roll_no}"


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)