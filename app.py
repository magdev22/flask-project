from flask import Flask, render_template, request
from models import Artist, Album, Song, db
import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение с базой данных

db.init_app(app)


@app.route('/<username>')

def index(username):
    return render_template('index.html', username=username )

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

@app.route('/time')

def time():
    now = datetime.datetime.now()
    if now.hour >= 6 and now.hour < 12:
        time = 'Доброе утро ' + str(now.hour)
    elif now.hour >= 12 and now.hour < 18:
        time = 'Добрый день ' + str(now.hour) + ':' + str(now.minute)
    elif now.hour >= 18 and now.hour < 24:
        time = 'Добрый вечер '
    else:
        time = 'Доброй ночи'
    return render_template('time.html', time=time)


if __name__ == '__main__':
    app.run(debug=True, port=9999)


