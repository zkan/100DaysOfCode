from flask import Flask, render_template

import requests


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    return data['value']


@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html',
                           title='Chuck Norris Jokes!',
                           joke=joke)


if __name__ == '__main__':
    app.run(debug=True)
