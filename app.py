from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello World!"

@app.route('/about')

def about():
    return render_template('about.html')


@app.route('/user/<name>')

def user(name):
    return f"Привет юзер {name}"

@app.route('/userid/<int:id>')

def userid(id):
    return f"Айди этого юзера {id}"

@app.route('/user/login', methods=['GET', 'POST'])

def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return "вы вошли в систему как " + username

if __name__ == '__main__':
    app.run(debug=True, port=9999)


