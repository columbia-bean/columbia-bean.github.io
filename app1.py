import os

from flask import Flask, render_template, url_for, flash, request, redirect, send_from_directory
from werkzeug.utils import secure_filename

#UPLOAD_FOLDER= '/Users/breadou/workspace/Bean/flask/uploads'
UPLOAD_FOLDER= '/Users/breadou/workspace/Bean/static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/demo', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template('demo.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    filename = "/static/" + filename
    return render_template('demo.html', image=filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/demo')
def demo():
	return render_template('demo.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
	
