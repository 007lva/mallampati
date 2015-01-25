from flask import Flask, render_template
from detect_platform import detect_platform

#define flask routes
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photobooth')
def photobooth():
    dp = detect_platform()
    is_mobile = dp.os_platform_not_desktop()
    return render_template('photobooth.html', is_mobile = is_mobile)

if __name__ == '__main__':
	app.config["SECRET_KEY"] = "RaoulKnowsNothingBetter"
	app.run()
