from flask import Flask, render_template

app = Flask(__name__, static_folder='templates', static_url_path='')


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/contact')
def contact():  # put application's code here
    return render_template('contact.html')


