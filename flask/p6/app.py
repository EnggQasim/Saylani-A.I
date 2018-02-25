from flask import Flask, render_template, \
url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/aboutUs")
def about():
    return render_template('about.html')

app.run(debug=True)