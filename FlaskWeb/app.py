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

l1='green'
l2='red'
l3='red'
l4='red'
c1=100
c2=40
c3=70
c4=20

@app.route('/display')
def display():
    return render_template('display.html',l1=l1,l2=l2,l3=l3,l4=l4,c1=c1,c2=c2,c3=c3,c4=c4)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)