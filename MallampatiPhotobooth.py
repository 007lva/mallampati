import os
from flask import Flask, render_template, request,\
    redirect, url_for, send_from_directory
from detect_platform import detect_platform
from werkzeug import secure_filename

#define flask config variables
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
app = Flask(__name__)
app.config["SECRET_KEY"] = "RaoulKnowsNothingBetter"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # uploads <= 20Mo

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/photobooth')
def photobooth():
    dp = detect_platform()
    is_mobile = dp.os_platform_not_desktop()
    if is_mobile == False:
        return render_template('photobooth.html')
    else:
        return render_template('photobooth_mobile_footer.html')
        
@app.route('/photobooth', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename = filename))

if __name__ == '__main__':
    app.run(debug = True)
