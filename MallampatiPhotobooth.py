from flask import Flask, render_template, request

#get user agent
def os_platform_not_desktop():
    '''
    uses werkzeug classes to detect OS. I used that because I do not
    want android & iOS devices to get the default photobooth.
    Use browser capability detection such as modernizer for anything else.
    '''
    platform = request.user_agent.platform
    if (platform == 'android') or (platform == 'ipad') or (platform == 'iphone'):
        return True
    else:
        return False

#define flask routes
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photobooth')
def photobooth():
    is_mobile = os_platform_not_desktop()
    return render_template('photobooth.html', is_mobile = is_mobile)

if __name__ == '__main__':
	app.config["SECRET_KEY"] = "RaoulKnowsNothingBetter"
	app.run()
