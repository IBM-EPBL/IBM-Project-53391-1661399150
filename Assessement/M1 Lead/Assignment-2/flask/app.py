from flask import Flask;
from flask import render_template;

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('Login.html')

@app.route('/signup')
def show():
    return render_template('Register.html')