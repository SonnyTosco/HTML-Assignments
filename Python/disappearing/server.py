from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    print "turtle power"
    return render_template('index.html')
@app.route('/ninja/<color>')
def color(color):
    print "april"
    return render_template("ninja.html", username=username)
@app.route('/ninja')
def ninja()
app.run(debug=True)
