from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/global')
def global_page():
    return render_template('global.html')

@app.route('/advance/risk')
def risk_page():
    return render_template('Portfolio_Risk.html')

@app.route('/advance/hedging')
def hedging_page():
    return render_template('Portfolio_Hedging.html')