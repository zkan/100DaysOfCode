from flask import (
    Flask,
    render_template,
    request,
)

from data import fav_beer


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        beer = request.form['beer']
        fav_beer[name] = beer

    return render_template('index.html',
                           fav_beer=fav_beer)


if __name__ == '__main__':
    app.run(debug=True)
