from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

if __name__ == '__main__':
	print(dir(Flask))
	app.run(debug=True)