from werkzeug.utils import secure_filename
from flask import *
from datetime import datetime
import os

app = Flask(__name__)

#File Upload

@app.route('/upload', methods = ['GET', 'POST'])
def render_file():
  files = os.listdir("./uploads")
  return render_template('upload.html', files =files)

@app.route('/fileUploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save('./uploads/' + filename)
      return redirect('/upload')
#File Download
@app.route('/downfile')
def down_page():    
    files = os.listdir('./uploads')
    return render_template('download.html', files = files)

@app.route('/downloadfile', methods = ['GET', 'POST'])
def file_download():
    if request.method == 'POST':
        sw = 0
        files = os.listdir("./uploads")
        for x in files:
            if(x == request.form['file']):
                sw=1
        path = "./uploads/"
        return send_file(path + request.form['file'],
                attachment_filename = request.form['file'],
                as_attachment = True)


if __name__ == "__main__":
    app.run(debug=True)
