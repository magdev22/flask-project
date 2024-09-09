from flask import Flask, render_template, request
from models import Artist, Album, Song, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение с базой данных

db.init_app(app)


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

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return "вы вошли в систему как " + username


@app.route('/songs')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)

if __name__ == '__main__':
    app.run(debug=True, port=9999)


