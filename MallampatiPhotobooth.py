#==============================================================================
# Imports
#==============================================================================
import os, imghdr
from flask import Flask, render_template, request, flash,\
    redirect, url_for, send_from_directory
from detect_platform import detect_platform
from werkzeug import secure_filename

#==============================================================================
# Globals & app config variables
#==============================================================================
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config["SECRET_KEY"] = "Rdged65742%"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # uploads <= 20Mo

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#==============================================================================
# Routing error handlers
#==============================================================================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

#==============================================================================
# Standard app routes
#==============================================================================
@app.route('/')
def index():
    return render_template('index.html')

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
    """
    Controls the form on the photobooth page, used to post images.
    """
    if request.method == 'POST':
        file = request.files['file']
        mimetype = imghdr.what(file)  # required, since flask uses browser mime
        if file and allowed_file(file.filename)\
        and mimetype in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename = filename))
        elif not file.filename:
            return redirect(url_for('photobooth'))
        else:
            flash('The file format provided is not supported.')
            return redirect(url_for('photobooth'))

@app.route('/show/<filename>')
def uploaded_file(filename):
    return render_template('upload.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug = True)
