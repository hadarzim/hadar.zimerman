from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/assignment8')
def assig8():
    found = True
    if found:
        return render_template('assignment8.html',
                               profile={'name': 'hadar', 'last_name': 'zimerman'},
                               university='BGU',
                               degrees=['B.A'],
                               hobbies=('play tennis','baking','run'))

    else:
        return render_template('assignment8.html')



@app.route('/home')
@app.route('/')
def home_func():
    found=True
    if found:
        return render_template('home.html', name='hadar')
    else:
        return render_template('home.html')


@app.route('/more')
def about_func():
    return render_template('more.html')

@app.route('/catalog')
def catalog_func():
    return render_template('catalog.html')

if __name__ == '__main__':
    app.run(debug=True)
