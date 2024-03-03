from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] =5 * 1024 * 1024 * 1024  #5GB (to resolve uploaded error(request entity too large))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        for i in range(1, 5):
            video = request.files.get(f'video{i}')
            if video:
                video.save(f'C:/Python/FlaskWeb/static/videos/video{i}.mp4')
        return redirect(url_for('display'))

    return render_template('upload.html')

n="red"

@app.route('/display')
def display():
    return render_template('display.html',n=n)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)