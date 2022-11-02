from datetime import datetime
import pytz
from flask import Flask
from flask import Flask, request, render_template, make_response, redirect, url_for, Response, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
	
	datetime_proper= datetime.now(pytz.timezone('Europe/London'))
	datetime_central = datetime.now(pytz.timezone('America/Chicago'))
	datetime_eastern = datetime.now(pytz.timezone('America/New_York'))
	datetime_onguardforthee = datetime.now(pytz.timezone('America/Vancouver'))
	datetime_norge = datetime.now(pytz.timezone('Europe/Oslo'))


	proper = datetime_proper.strftime('%H:%M')
	central = datetime_central.strftime('%H:%M')
	eastern = datetime_eastern.strftime('%H:%M')
	onguardforthee = datetime_onguardforthee.strftime('%H:%M')
	norge = datetime_norge.strftime('%H:%M')

	return render_template("index.html", proper=proper, eastern=eastern, central=central, onguardforthee=onguardforthee, norge=norge)

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

	return render_template("index.html")


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)


# Salem, eastern - America/New_York
# texas, central - America/Chicago