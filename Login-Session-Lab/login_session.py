from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		request.form['quote'] = quote
		request.form['author'] = author
		request.form['age'] = age
		return render_template('home.html')
	return redirect(url_for('thanks'))


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', ) # What variables are needed?


@app.route('/thanks' , )
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)