from flask import Flask, render_template, url_for, send_from_directory, request, flash, redirect


app = Flask(__name__)



#Homepage for the app
@app.route("/")
def homepage():
  #you can add functions here to gather information like time, temperature, weather and pass them to the template in the return function
  return render_template('homepage.html', title='Hey Pat')

@app.route("/secondpage")
def anotherpage():
  #same concept applies here. add stuff here and pass it to a html template.
  return render_template('homepage.html', title='Nothing')
