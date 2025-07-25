import random
import string
import pymysql
import redis
import json
from flask import Flask, render_template, redirect, request, jsonify, session
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

MYSQL_SERVER_ENDPOINT = os.environ['MYSQL_SERVER_ENDPOINT']
MYSQL_SERVER_USERNAME = os.environ['MYSQL_SERVER_USERNAME']
MYSQL_SERVER_PASSWORD = os.environ['MYSQL_SERVER_PASSWORD']
MYSQL_SERVER_DATABASE = os.environ['MYSQL_SERVER_DATABASE']
MYSQL_SERVER_PORT = int(os.environ['MYSQL_SERVER_PORT'])
MYSQL_SERVER_CHARSET = os.environ['MYSQL_SERVER_CHARSET']
REDIS_SERVER_ENDPOINT = os.environ['REDIS_SERVER_ENDPOINT']
REDIS_SERVER_PORT = int(os.environ['REDIS_SERVER_PORT'])
REDIS_SERVER_CHARSET = os.environ['REDIS_SERVER_CHARSET']
REDIS_SERVER_SHORTURL_TIMEOUT = int(os.environ['REDIS_SERVER_SHORTURL_TIMEOUT'])
URLSHORT_SERVER_PORT=int(os.environ['URLSHORT_SERVER_PORT'])

def redis_database():
    redisCli = redis.Redis(
        host=REDIS_SERVER_ENDPOINT,
        port=REDIS_SERVER_PORT,
        # charset=REDIS_SERVER_CHARSET,
        decode_responses=True
        )
    return redisCli

def get_connection():
    conn = pymysql.connect(
        host=MYSQL_SERVER_ENDPOINT,
        port=MYSQL_SERVER_PORT,
        user=MYSQL_SERVER_USERNAME,
        password=MYSQL_SERVER_PASSWORD,
        db=MYSQL_SERVER_DATABASE,
        charset=MYSQL_SERVER_CHARSET,
        cursorclass=pymysql.cursors.DictCursor
        )
    return conn

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url

def insert_url_to_database(long_url, short_url, users_email):
    con = None
    try:
        con = get_connection()
        with con.cursor() as cur:
            cur.execute(
                "INSERT INTO urls (link, short_url, email) VALUES (%s, %s, %s)",
                (long_url, short_url, users_email)
                )
            con.commit()
    except Exception as e:
        print(f"Error inserting URL to database: {e}")
    finally:
        if con:
            con.close()

def redirectShortUrl(short_url):
    try:
        con = get_connection()
        with con.cursor() as cur:
            cur.execute(
                "UPDATE urls SET visitors=visitors+1 WHERE short_url = %s",
                (short_url,)
                )
            con.commit()
    except Exception as e:
        print(f"Error inserting URL to database: {e}")
        return {
            "msg": f"Error inserting URL to database: {e}"
        }
    finally:
        if con:
            con.close()

def allurls():
    try:
        con = get_connection()
        with con.cursor() as cur:
            cur.execute("SELECT * FROM urls")
            data = cur.fetchall()
            if data:
                return jsonify(data), 200
            return jsonify({
                "error": "No data found"
                }), 404
    except Exception as e:
        print(f"Error : {e}")
    finally:
        if con:
            con.close()

@app.route("/api/url", methods=["POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        users_email = request.form['users_email']
        short_url = generate_short_url()
        insert_url_to_database(
            long_url,
            short_url,
            users_email
            )
        return jsonify({
            "long_url": long_url,
            "short_url": short_url
            }), 200

@app.route("/r/<short_url>")
def redirect_url(short_url):
    try:
        con = get_connection()
    except pymysql.err.OperationalError:
        return render_template(
            "internal_server_error.html",
            msg="MySQL Database issue"
            )
    redis_server = redis_database()
    try:
        if redis_server.get(short_url) is None:
            cur = con.cursor()
            cur.execute(
                'SELECT * FROM urls WHERE short_url = %s;',
                (short_url)
                )
            result = cur.fetchall()
            if result:
                row = result[0]
                long_url = (row['link'])
                try:
                    redis_server.setex(
                        short_url,
                        REDIS_SERVER_SHORTURL_TIMEOUT,
                        value = json.dumps(row)
                        )
                except:
                    print(f'The short URL {short_url} has not been added to redis')
            redirectShortUrl(short_url)
            cur.close()
            con.close()
            return redirect(long_url)
    except redis.exceptions.ConnectionError:
            cur = con.cursor()
            cur.execute('SELECT * FROM urls WHERE short_url = %s;', (short_url,))
            result = cur.fetchall()
            if result:
                row = result[0]
                long_url = (row['link'])
            redirectShortUrl(short_url)
            cur.close()
            con.close()
            return redirect(long_url)
    else:
        try:
            redis_value =  json.loads(redis_server.get(short_url))
        except:
            return render_template(
                "internal_server_error.html",
                msg="Redis Issue"
                )
        original_url = redis_value['link']
        redirectShortUrl(short_url)
        return redirect(original_url)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',  port=URLSHORT_SERVER_PORT)