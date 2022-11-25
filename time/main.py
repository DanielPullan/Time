from datetime import datetime
import pytz
from flask import Flask
from flask import Flask, request, render_template, make_response, redirect, url_for, Response, redirect, url_for
import sys


app = Flask(__name__)

# Setting for custom port support. If you'd like to use a port other than 5000, just set an argument when running time.
# Example: 'poetry run python3 time/main.py 6000' will run on port 6000
# Example: 'poetry run python3 time/main.py' will run on port 5000 as it's the default.
try:
	exposeport = sys.argv[1]
except	:
	exposeport = 5000


@app.route('/')
def index():
	# If there's no cookies set, use everything in the if statement as default options.
	if request.cookies.get('option1') == None:
		option1 = 'Europe/London'
		option1name = 'London'
		option1emoji = '🇬🇧'
		option2 = 'Europe/Dublin'
		option2name = 'Dublin'
		option2emoji = '🇮🇪'
	# Otherwise, get the data from the cookies set and get them ready for use in variables.
	else:
		option1 = request.cookies.get('option1')
		option1name = request.cookies.get('option1name')
		option1emoji = request.cookies.get('option1emoji')
		option2 = request.cookies.get('option2')
		option2name = request.cookies.get('option2name')
		option2emoji = request.cookies.get('option2emoji')

	
	# Get the time for the default locations
	datetime_uk= datetime.now(pytz.timezone('Europe/London'))
	datetime_central = datetime.now(pytz.timezone('America/Chicago'))
	datetime_eastern = datetime.now(pytz.timezone('America/New_York'))
	datetime_onguardforthee = datetime.now(pytz.timezone('America/Vancouver'))
	datetime_norge = datetime.now(pytz.timezone('Europe/Oslo'))

	# Get the time for the custom options
	datetime_option1 = datetime.now(pytz.timezone(option1))
	datetime_option2 = datetime.now(pytz.timezone(option2))

	# Format the time for both default and custom locations
	uk = datetime_uk.strftime('%H:%M')
	central = datetime_central.strftime('%H:%M')
	eastern = datetime_eastern.strftime('%H:%M')
	onguardforthee = datetime_onguardforthee.strftime('%H:%M')
	norge = datetime_norge.strftime('%H:%M')
	option1 = datetime_option1.strftime('%H:%M')
	option2 = datetime_option2.strftime('%H:%M')

	# Fancy lists for the custom options. This limits the amount of variables to return in the page.
	option1list = [option1, option1name, option1emoji]
	option2list = [option2, option2name, option2emoji]

	# Return the index template and let it access all of this data within the page for the templating stuff.
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
	app.run(host="0.0.0.0", port=exposeport	, debug=True)