from flask import Flask, render_template, request,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/videos'

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/upload')
def upload():
   return render_template('upload.html')


@app.route('/display')
def display():
   return render_template('display.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], "UploadedVideo.mp4"))
      
      return redirect('/display')

if __name__ == '__main__':
   app.run(debug = True)
