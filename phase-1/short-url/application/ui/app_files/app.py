import random
import string
import requests
import json
from flask import Flask, render_template, redirect, request, url_for, session, jsonify
from functools import wraps
import os

app = Flask(__name__)

SHORTURL_GENERATED_URL = os.environ['SHORTURL_GENERATED_URL']
app.secret_key = os.environ['SESSION_SECRET_KEY']
AUTH_SERVER_URL = os.environ['AUTH_SERVER_URL']
AUTH_SERVER_LOGIN_API = os.environ['AUTH_SERVER_LOGIN_API']
AUTH_SERVER_USER_API = os.environ['AUTH_SERVER_USER_API']
AUTH_SERVER_REGISTER_API = os.environ['AUTH_SERVER_REGISTER_API']
# NOTIFY_SERVER_URL = os.environ['NOTIFY_SERVER_URL']
# NOTIFY_USER_REGISTER_API = os.environ['NOTIFY_USER_REGISTER_API']
# NOTIFY_USER_LOGIN_API = os.environ['NOTIFY_USER_LOGIN_API']
# NOTIFY_USER_ALLURLS_API = os.environ['NOTIFY_USER_ALLURLS_API']
# NOTIFY_USER_SHORTURLS_API = os.environ['NOTIFY_USER_SHORTURLS_API']
SHORTURL_SERVER_URL = os.environ['SHORTURL_SERVER_URL']
SHORTURL_SERVER_URL_API = os.environ['SHORTURL_SERVER_URL_API']
REPORT_SERVER_URL = os.environ['REPORT_SERVER_URL']
REPORT_SERVER_REPORT_API = os.environ['REPORT_SERVER_REPORT_API']
UI_SERVER_PORT = int(os.environ['UI_SERVER_PORT'])

def token_required(func):
	@wraps(func)
	def decorated(*args, **kwargs):
		token = request.cookies['session']
		if not token:
			return jsonify({
				'Alert!': 'Token is missing!'
				}), 401
		try:
			username_session_data = session.get('username')
			password_session_data = session.get('password')
		except 'BadRequestKeyError':
			return jsonify({
				'Alert!': 'Session Cookie is missing!'
				}), 401
		try:
			account = requests.get(
				f"{AUTH_SERVER_URL}{AUTH_SERVER_LOGIN_API}",
				json = {
				"username": username_session_data,
				"password": password_session_data
				})
			if account.status_code != 200 and account.status_code != 500:
				return jsonify({
					'Message': 'Invalid token'
					}), 403
			if account.status_code == 500:
				return render_template(
					"internal_server_error.html",
					msg =account.content
					)
		except:
			return jsonify({
				'Message': 'Invalid token'
				}), 403
		return func(*args, **kwargs)
	return decorated


@app.route("/", methods=["GET", "POST"])
def index():
	shortened_url = None
	if request.method == "POST":
		long_url = request.form['long_url']
		parameters = {
			"long_url": long_url
			}
		returnResponse = requests.post(
			f"{SHORTURL_SERVER_URL}{SHORTURL_SERVER_URL_API}",
			parameters
			)
		short_url = returnResponse.json()["short_url"]
		shortened_url = f"http://{SHORTURL_GENERATED_URL}/r/{short_url}"
		return render_template(
			"short_url.html",
			shortened_url=shortened_url
			)
	return render_template(
		"index.html",
		shortened_url=shortened_url
		)

@app.route('/signup', methods=["GET", "POST"])
def register():
	if request.method == "POST":
		email = request.form["email"]
		password = request.form["password"]
		username = request.form["username"]
		if email == '' or password == '' or username == '':
			return render_template(
				'register.html',
				msg="Provide all parameters to register"
				), 200
		else:
			account = requests.post(
				f"{AUTH_SERVER_URL}{AUTH_SERVER_REGISTER_API}",
				json = {
				"email": email,
				"password": password,
				"username": username
			})
			if account.status_code == 200:
				print("notifyapi")
				# notify_register = requests.post(
				# 	f"{NOTIFY_SERVER_URL}{NOTIFY_USER_REGISTER_API}",
				# 	json = {
				# 	"email": email,
				# 	"password": password,
				# 	"username": username
				# })
			elif account.status_code == 500 and account.json()["msg"] == "user exists":
				return render_template(
					"signup.html",
					msg="User already registerd"
				)
			else:
				return render_template("internal_server_error.html")
		return redirect(url_for("login"))
	return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		account = requests.get(
			f"{AUTH_SERVER_URL}{AUTH_SERVER_LOGIN_API}",
			json = {
			"username": username,
			"password": password
			})
		userDataVar = account.json()
		if account.status_code == 200:
			session['loggedin'] = True
			session['username'] = userDataVar['username']
			session['password'] = userDataVar['password']
			session['email'] = userDataVar['email']
			# notify_email =  userDataVar['email']
			# notify_login = requests.post(
			# 	f"{NOTIFY_SERVER_URL}{NOTIFY_USER_LOGIN_API}",
			# 	json = {
			# 	"Username": userDataVar['username'],
			# 	"Email": userDataVar['email']
			# 	})
			return render_template("home.html")
		else:
			emailReqVar = requests.get(
				f"{AUTH_SERVER_URL}{AUTH_SERVER_USER_API}",
				json = {
				"username": username
				})
			if emailReqVar.status_code != 200 and emailReqVar.status_code != 500:
				return render_template(
					'login.html',
					msg="username doesnot exists !!"
					), 302
			if emailReqVar.status_code != 200 and emailReqVar.status_code == 500:
				return render_template("internal_server_error.html")
			return render_template(
				'login.html',
				msg="username & Password doesnot match !!"
				), 302
	return render_template("login.html")

@app.route("/home")
@token_required
def home():
	return render_template("home.html")

@app.route("/short", methods=["GET", "POST"])
@token_required
def short():
	shortened_url = None
	if request.method == "POST":
		users_email = session.get("email")
		long_url = request.form['long_url']
		parameters = {
			"long_url": long_url,
			"users_email": users_email
		}
		headers = {
			'Content-Type': 'application/json'
			}
		returnResponse = requests.post(
			f"{SHORTURL_SERVER_URL}{SHORTURL_SERVER_URL_API}",
			parameters
			)
		short_url = returnResponse.json()["short_url"]
		shortened_url = f"http://{SHORTURL_GENERATED_URL}/r/{short_url}"
		return render_template(
			"short_url.html",
			shortened_url=shortened_url
			)
	return render_template(
		"short.html",
		shortened_url=shortened_url
		)

@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for("index"))

@app.route("/report", methods=["GET", "POST"])
@token_required
def report():
	users_email = session.get("email")
	response = requests.get(
		f'{REPORT_SERVER_URL}{REPORT_SERVER_REPORT_API}',
		json={
			'email': users_email
			}
		)
	if response.status_code == 200:
		data = response.json()
		return render_template(
			"report.html",
			data=data
			)
	elif response.status_code == 500:
		return render_template("internal_server_error.html")
	else:
		error_message = f"Error fetching data: {response.json().get('error')}"
		return render_template("report.html", error=error_message)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=UI_SERVER_PORT)