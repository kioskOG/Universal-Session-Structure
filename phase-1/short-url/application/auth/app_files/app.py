"""
This application is used to register and authenticate user
"""

import os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector
import pymysql
from prometheus_client import Summary, Counter, Gauge, generate_latest
import time


server = Flask(__name__)

MYSQL_SERVER_ENDPOINT = os.environ['MYSQL_SERVER_ENDPOINT']
MYSQL_SERVER_USERNAME = os.environ['MYSQL_SERVER_USERNAME']
MYSQL_SERVER_PASSWORD = os.environ['MYSQL_SERVER_PASSWORD']
MYSQL_SERVER_DATABASE = os.environ['MYSQL_SERVER_DATABASE']

server.config['MYSQL_HOST'] = MYSQL_SERVER_ENDPOINT
server.config['MYSQL_USER'] = MYSQL_SERVER_USERNAME
server.config['MYSQL_PASSWORD'] = MYSQL_SERVER_PASSWORD
server.config['MYSQL_DB'] = MYSQL_SERVER_DATABASE

mysqlVar = MySQL(server)

# Prometheus metrics
REQUEST_TIME = Summary('login_request_processing_seconds', 'Time spent processing login request')
REQUEST_COUNT = Counter('login_request_count', 'Number of login requests')
IN_PROGRESS = Gauge('login_in_progress_requests', 'In-progress login requests')
REQUEST_FAILURES = Counter('login_request_failures', 'Number of failed login requests')


@server.route('/auth/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}


@server.route('/api/v1/auth/login', methods=['GET'])
@REQUEST_TIME.time()
def login():
    """
    Authenticates a user using provided username and password.

    Returns:
        JSON response containing user details if authentication is successful,
        otherwise an error message.
    """
    REQUEST_COUNT.inc()
    IN_PROGRESS.inc()

    username = request.json['username']
    password = request.json['password']
    try:
        connection = pymysql.connect(
            host=MYSQL_SERVER_ENDPOINT,
            user=MYSQL_SERVER_USERNAME,
            password=MYSQL_SERVER_PASSWORD,
            database=MYSQL_SERVER_DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.err.OperationalError:
        REQUEST_FAILURES.inc()
        IN_PROGRESS.dec()
        return jsonify({
            "msg": "Unknown MySQL server host"
        }), 500
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM users WHERE username = %s AND password = %s',
        (username, password)
        )
    account = cursor.fetchone()
    if account is None:
        REQUEST_FAILURES.inc()
        IN_PROGRESS.dec()
        return jsonify({'Msg': 'Wrong Credentials!'}), 403
    IN_PROGRESS.dec()
    return jsonify({
        "username": account['username'],
        "password": account['password'],
        "email": account['email']
        }), 200

@server.route('/api/v1/auth/user', methods=['GET'])

def usercheck():
    """
    Checks if a user exists in the database.

    Returns:
        JSON response containing the username if user exists,
        otherwise an error message.
    """
    username = request.json['username']
    try:
        cursor = mysqlVar.connection.cursor(MySQLdb.cursors.DictCursor)
    except MySQLdb.OperationalError:
        return jsonify({
            "msg": "Unknown MySQL server host"
        }), 500
    cursor.execute(
        'SELECT * FROM users WHERE username = %s',
        [username]
        )
    account = cursor.fetchone()
    if account is None:
        return jsonify({
            'Msg': 'username doesnot exists !!'
            }), 403
    return jsonify({
        "username": account['username']
    }), 200

@server.route('/api/v1/auth/register', methods=['POST'])

def register():
    """
    Registers a new user with provided email, username, and password.

    Returns:
        JSON response containing the email if registration is successful,
        otherwise an error message.
    """
    REQUEST_COUNT.inc()
    IN_PROGRESS.inc()

    email = request.json['email']
    password = request.json['password']
    username = request.json['username']
    try:
        mydb = mysql.connector.connect(
            host=MYSQL_SERVER_ENDPOINT,
            user=MYSQL_SERVER_USERNAME,
            password=MYSQL_SERVER_PASSWORD,
            database=MYSQL_SERVER_DATABASE
        )
    except mysql.connector.errors.DatabaseError:
        REQUEST_FAILURES.inc()
        IN_PROGRESS.dec()
        return jsonify({
            "msg": "Unknown MySQL server host"
        }), 500
    mycursor = mydb.cursor()
    try:
        mycursor.execute(
            'INSERT INTO users (email,password,username) VALUES(%s, %s, %s)',
            (email,password,username)
            )
    except mysql.connector.Error as my_error:
        if "Duplicate" in my_error.msg:
            REQUEST_FAILURES.inc()
            IN_PROGRESS.dec()
            return jsonify({
                "msg": "user exists"
            }), 500
    mydb.commit()
    IN_PROGRESS.dec()
    return jsonify({
        "email": email
    }), 200

if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=5000)
