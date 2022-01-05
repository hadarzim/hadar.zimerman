from flask import Flask, redirect, url_for, request, Blueprint
from flask import render_template
from flask import session
from interact_with_DB import interact_db


assignment10 = Blueprint('assignment10',
                         __name__,
                         static_folder='/static',
                         template_folder='templates')


@assignment10.route ('/assignment10')
def user_func():
    query = "select * from users"
    query_result = interact_db(query=query,query_type='fetch')
    return render_template('assignment10.html', users=query_result)



@assignment10.route('/insert_user', methods=['GET','POST'])
def insert_user_func():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        query = "INSERT INTO users(name, email, password) VALUES ('%s','%s','%s')" % (name, email, password)
        interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@assignment10.route('/update_Name', methods=['GET', 'POST'])
def nameupdate():
    if request.method == 'POST':
        user_id = request.form['id']
        name = request.form['name']
        query = "UPDATE users SET name='%s' WHERE id='%s' ;" % (name, user_id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return redirect('/assignment10')

@assignment10.route('/update_Email', methods=['GET', 'POST'])
def emailupdate():
    if request.method == 'POST':
        user_id = request.form['id']
        email = request.form['email']
        query = "UPDATE users SET email='%s' WHERE id='%s' ;" % (email, user_id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return redirect('/assignment10')

@assignment10.route('/delete_user', methods=['GET','POST'])
def delete_user_func():
    if request.method == 'GET':
        user_id = request.args['id']
        query = "DELETE FROM users WHERE id='%s';" % user_id
        interact_db(query, query_type='commit')
        return redirect('/assignment10')
    return redirect('/assignment10')



