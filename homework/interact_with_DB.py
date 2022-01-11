from flask import jsonify
import mysql.connector
import json

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

def query_to_json(query):
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskprojectdb')
    #  db cursor - this object executes sql queries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()

    connection.close()
    cursor.close()
    return result