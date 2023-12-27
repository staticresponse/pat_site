from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
  #Custom code goes here
  return render_template('example.html')
