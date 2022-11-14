from datetime import datetime
import pytz
from flask import Flask
from flask import Flask, request, render_template, make_response, redirect, url_for, Response, redirect, url_for


app = Flask(__name__)



name="Noisy"

@app.route('/')
def index():

	option1 = "Europe/London"
	option1name = "London"
	option2 = "Europe/Dublin"
	option2name= "dublin"

	
	option1 = request.cookies.get('option1')
	option2 = request.cookies.get('option2')
	option1name = request.cookies.get('option1name')
	option2name = request.cookies.get('option2name')

	
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



	return render_template("index.html", uk=uk, eastern=eastern, central=central, onguardforthee=onguardforthee, norge=norge, option1=option1, option1name=option1name, option2=option2, option2name=option2name)

@app.route('/dos')
def dos():
	
	# Use for testing.

	# Thoughts would be something like 
	# 1. record user preference on timezones and names of those locations
	# 2. return as a view
	# 3. be able to modify those preferneces


	# so maybe something like "on first load, get the preferences (europe/london is "home", europe/oslo "meeting") record this as a cookie. On page load, send preference to flask, get the data, return in template. page loads remembering this. Click on "edit" to go to /modify, to wipe the preferences and start over again.
	# this requires a simple local cookie, but nothing needs to be recorded on a server.
	# may need to self host a API location thingy, or expect user to know the name of the tz that they need
	# would also be cool to record a preference for emoji or text, as well as the description

	return render_template("index.html")

@app.route('/setsetset')
def setsetset():
   return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
	   option1 = request.form['option1']
	   option1name = request.form['option1name']

	   option2 = request.form['option2']
	   option2name = request.form['option2name']
	   
	   resp = make_response(redirect('/'))
	   resp.set_cookie('option1', option1)
	   resp.set_cookie('option1name', option1name)
	   resp.set_cookie('option2', option2)
	   resp.set_cookie('option2name', option2name)
   
   return resp


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)


# Salem, eastern - America/New_York
# texas, central - America/Chicago