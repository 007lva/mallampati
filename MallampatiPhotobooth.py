from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photobooth')
def photobooth():
    return render_template('photobooth.html')

if __name__ == '__main__':
	app.config["SECRET_KEY"] = "RaoulKnowsNothingBetter"
	app.run()
