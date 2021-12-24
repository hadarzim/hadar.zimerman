from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '12345'


@app.route('/assignment8')
def assig8():
    found = True
    if found:
        return render_template('assignment8.html',
                               profile={'name': 'hadar', 'last_name': 'zimerman'},
                               university='BGU',
                               degrees=['B.A'],
                               hobbies=('play tennis', 'baking', 'run'))

    else:
        return render_template('assignment8.html')


@app.route('/home')
@app.route('/')
def home_func():
    found = True
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

@app.route('/logout')
def logout_func():
    session['username']=''
    return render_template('home.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def assig9_func():
    if request.method == 'GET':
        if 'username' in request.args:
            username = request.args['username']
            found = True
            if found:
                session['username'] = username
            if username == '':
                return render_template('assignment9.html',
                                       users={'user1': {'username': 'hadar', 'email': 'hadar@gmail.com'},
                                              'user2': {'username': 'dani', 'email': 'dani@gmail.com'},
                                              'user3': {'username': 'shelly', 'email': 'shelly@gmail.com'},
                                              'user4': {'username': 'gal', 'email': 'gal@gmail.com'},
                                              'user5': {'username': 'eyal', 'email': 'eyal@gmail.com'},
                                              'user6': {'username': 'ron', 'email': 'ron@gmail.com'}})
            else:
                return render_template('assignment9.html', username=username,
                                       users={'user1': {'username': 'hadar', 'email': 'hadar@gmail.com'},
                                              'user2': {'username': 'dani', 'email': 'dani@gmail.com'},
                                              'user3': {'username': 'shelly', 'email': 'shelly@gmail.com'},
                                              'user4': {'username': 'gal', 'email': 'gal@gmail.com'},
                                              'user5': {'username': 'eyal', 'email': 'eyal@gmail.com'},
                                              'user6': {'username': 'ron', 'email': 'ron@gmail.com'}})

        else:
            return render_template('assignment9.html')
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        found = True
        if found:
            session['username'] = username
            return render_template('home.html', name=username)
        else:
            return render_template('assignment9.html')
    if 'username' in request.args:
        user = request.args['username']
        return render_template('assignment9.html', p_name=user)
    return render_template('assignment9.html')

@app.route ('/users')
def user_func():
    query = "select * from users"
    query_result = interact_db(query=query,query_type='fetch')
    return render_template('users.html', users=query_result)

@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    query = "INSERT INTO users(name, email, password) VALUES ('%s','%s','%s')" % (name, email, password)
    interact_db(query=query, query_type='commit')
    return redirect('/users')

@app.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query, query_type='commit')
    return redirect('/users')
