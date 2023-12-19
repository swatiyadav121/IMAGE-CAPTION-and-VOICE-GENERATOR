from flask import Flask,render_template,request,redirect, url_for
from werkzeug.utils import secure_filename
from predict import predict
import gtts
from playsound import playsound
from flask import send_file

app = Flask(__name__)

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/hello.mp3')
def song_mp3():
    return send_file('hello.mp3', attachment_filename='hello.mp3')

@app.route('/', methods = ['GET', 'POST'])
def services():
	if request.method == 'POST':
		ans="\""
		f = request.files['file']
		f.filename="pritika.jpg"
		f.save("static/img/"+f.filename)
		ans=ans+predict("static/img/pritika.jpg").title()+"\""
		print("ANSWWRRRRR ISS",ans)
		tts = gtts.gTTS(ans)
		tts.save("hello.mp3")
		playsound("hello.mp3")
		return render_template("services.html",ans=ans)
	return render_template("services.html")

@app.route('/single')
def single():
	return render_template("single.html")


if __name__ == '__main__':
    app.run(host="localhost", port=7000, debug=True)