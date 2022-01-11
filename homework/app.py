from random import random
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
from interact_with_DB import interact_db, query_to_json
import mysql.connector
import requests
import json


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


@app.route('/logout')
def logout_func():
    session['username']=''
    return render_template('home.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
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
    if request.method == 'POST':
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

from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

#
# @app.route ('/users')
# def user_func():
#     query = "select * from users"
#     query_result = interact_db(query=query,query_type='fetch')
#     return render_template('users.html', users=query_result)
#
#
# @app.route('/insert_user', methods=['GET','POST'])
# def insert_user_func():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         query = "INSERT INTO users(name, email, password) VALUES ('%s','%s','%s')" % (name, email, password)
#         interact_db(query=query, query_type='commit')
#     return redirect('/users')
#
# @app.route('/update_Name', methods=['GET', 'POST'])
# def nameupdate():
#     if request.method == 'POST':
#         user_id = request.form['id']
#         name = request.form['name']
#         query = "UPDATE users SET name='%s' WHERE id='%s' ;" % (name, user_id)
#         interact_db(query=query, query_type='commit')
#         return redirect('/users')
#     return redirect('/users')
#
# @app.route('/update_Email', methods=['GET', 'POST'])
# def emailupdate():
#     if request.method == 'POST':
#         user_id = request.form['id']
#         email = request.form['email']
#         query = "UPDATE users SET email='%s' WHERE id='%s' ;" % (email, user_id)
#         interact_db(query=query, query_type='commit')
#         return redirect('/users')
#     return redirect('/users')
#
# @app.route('/delete_user', methods=['GET','POST'])
# def delete_user_func():
#     if request.method == 'GET':
#         user_id = request.args['id']
#         query = "DELETE FROM users WHERE id='%s';" % user_id
#         interact_db(query, query_type='commit')
#         return redirect('/users')
#     return redirect('/users')





def interact_db(query,query_type:str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskprojectdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value=True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# @app.route('/req_frontend')
# def req_frontend_func():
#     return render_template('req_frontend.html')



# @app.route('/req_backend')
# def req_backend_func():
#     num = 3
#     if "number" in request.args:
#         num = int(request.args['number'])
#     pockemons = get_pockemons(num)
#     return render_template('req_backend.html')
#
# def get_pockemons(num):
#     pockemons = []
#     for i in range(num):
#         random_n = random.randint(1, 100)
#         res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_n}')
#         res = res.json()
#         pockemons.append(res)
#     return pockemons

# @app.route('/req_frontend')
# def getUser_func():
#     return render_template('req_frontend.html')
#

@app.route("/assignment11/users")
def assignment11_page():
    query = "select * from users"
    query_result = query_to_json(query=query)
    return json.dumps(query_result)

#  4+5
@app.route("/assignment11/outer_source", methods=['GET'])
def assignment11_os_page():
    if 'number' in request.args:
        number = request.args['number']
        res = requests.get(url=f"https://reqres.in/api/users/{number}")
        res = res.json()
        return render_template('assignment11.html', user=res['data'])
    return render_template('assignment11.html')


if __name__ == '__main__':
    app.run(debug=True)