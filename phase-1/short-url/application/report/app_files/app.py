from flask import Flask, request, session, jsonify
from functools import wraps
import pymysql
import os

app = Flask(__name__)

MYSQL_SERVER_ENDPOINT = os.environ['MYSQL_SERVER_ENDPOINT']
MYSQL_SERVER_USERNAME = os.environ['MYSQL_SERVER_USERNAME']
MYSQL_SERVER_PASSWORD = os.environ['MYSQL_SERVER_PASSWORD']
MYSQL_SERVER_DATABASE = os.environ['MYSQL_SERVER_DATABASE']
MYSQL_SERVER_PORT = int(os.environ['MYSQL_SERVER_PORT'])

def get_connection():
    conn = pymysql.connect(
        host=MYSQL_SERVER_ENDPOINT,
        port=MYSQL_SERVER_PORT,
        user=MYSQL_SERVER_USERNAME,
        password=MYSQL_SERVER_PASSWORD,
        db=MYSQL_SERVER_DATABASE,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
    return conn

@app.route("/report", methods=["GET", "POST"])
def report():
	users_email = request.json["email"]
	if users_email:
		con = get_connection()
		try:
			with con.cursor() as cur:
				query = "SELECT * FROM urls WHERE email = %s"
				cur.execute(query, (users_email,))
				data = cur.fetchall()
				if data:
					return jsonify(data), 200
				return jsonify({
					"error": "No data found"
					}), 404
		except Exception as e:
			print(e)
			return jsonify(
				f"Error : {e}"
				), 500
		finally:
			if con:
				con.close()

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)