from random import random
from flask import Flask, render_template, request, flash, redirect, url_for, session
##from models import

app = Flask(__name__)
app.secret_key = "group1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    Playerchoice = request.form['Player_choice']
    ComputerChoice = random.randint(1, 4)

    if Playerchoice == 1 or Playerchoice == 2 or Playerchoice == 3 or Playerchoice == 4:
        session['Player_choice']= Playerchoice
        session['Computer_choice'] = ComputerChoice
        return redirect(url_for('results'))
    else:
        flash("Invalid choice must be 1-4")

    return redirect(url_for('index'))

@app.route('/results')
def results():
    Playerchoice = session.get('Player_choice')
    ComputerChoice = session.get('Computer_choice')

    if Playerchoice and ComputerChoice:
        return render_template("results.html")


if __name__ == '__main__':
    app.run(debug=True)


