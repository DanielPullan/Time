from datetime import datetime
import pytz
from flask import Flask
from flask import Flask, request, render_template, make_response, redirect, url_for, Response, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():

	option1 = request.cookies.get('option1')
	option2 = request.cookies.get('option2')
	
	option1name = request.cookies.get('option1name')
	option2name = request.cookies.get('option2name')

	option1emoji = request.cookies.get('option1emoji')
	option2emoji = request.cookies.get('option2emoji')

	
	datetime_uk= datetime.now(pytz.timezone('Europe/London'))
	datetime_central = datetime.now(pytz.timezone('America/Chicago'))
	datetime_eastern = datetime.now(pytz.timezone('America/New_York'))
	datetime_onguardforthee = datetime.now(pytz.timezone('America/Vancouver'))
	datetime_norge = datetime.now(pytz.timezone('Europe/Oslo'))

	datetime_option1 = datetime.now(pytz.timezone(option1))
	datetime_option2 = datetime.now(pytz.timezone(option2))


	uk = datetime_uk.strftime('%H:%M')
	central = datetime_central.strftime('%H:%M')
	eastern = datetime_eastern.strftime('%H:%M')
	onguardforthee = datetime_onguardforthee.strftime('%H:%M')
	norge = datetime_norge.strftime('%H:%M')
	option1 = datetime_option1.strftime('%H:%M')
	option2 = datetime_option2.strftime('%H:%M')

	option1list = [option1, option1name, option1emoji]
	option2list = [option2, option2name, option2emoji]




	return render_template("index.html", uk=uk, eastern=eastern, central=central, onguardforthee=onguardforthee, norge=norge, option1list=option1list, option2list=option2list)

@app.route('/boxboxbox')
def boxboxbox():
   return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
	   option1 = request.form['option1']
	   option1name = request.form['option1name']
	   option1emoji = request.form['option1emoji']

	   option2 = request.form['option2']
	   option2name = request.form['option2name']
	   option2emoji = request.form['option2emoji']

	   option1list = [option1, option1name, option1emoji]
	   option2list = [option2, option2name, option2emoji]
	   
	   resp = make_response(redirect('/'))	
	   resp.set_cookie('option1', option1list[0])
	   resp.set_cookie('option1name', option1list[1])
	   resp.set_cookie('option1emoji', option1list[2])
	   resp.set_cookie('option2', option2list[0])
	   resp.set_cookie('option2name', option2list[1])
	   resp.set_cookie('option2emoji', option2list[2])

   
   return resp


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)