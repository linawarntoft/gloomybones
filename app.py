from flask import Flask, render_template
from data import Prints

app = Flask(__name__, static_url_path='/static')

Prints = Prints()

@app.route('/') #decorator
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/prints')
def prints():
	return render_template('prints.html', prints = Prints)
	
@app.route('/print/<string:id>/')
def oneprint(id):
	return render_template('print.html', id = id)
	

if __name__ == '__main__':
	app.run(debug=True)