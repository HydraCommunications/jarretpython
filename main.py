from random import randint
from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "group1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    player_choice = request.form['Player_choice']
    computer_choice = randint(1, 4)

    if player_choice in ['1', '2', '3', '4']:
        session['player_choice'] = int(player_choice)
        session['computer_choice'] = computer_choice
        return redirect(url_for('results'))
    else:
        flash("Invalid choice. Must be 1-4")
        return redirect(url_for('index'))

@app.route('/results')
def results():
    player_choice = session.get('player_choice')
    computer_choice = session.get('computer_choice')

    if player_choice is not None and computer_choice is not None:
        return render_template("results.html", player_choice=player_choice, computer_choice=computer_choice)
    else:
        flash("No game data found. Please play the game first.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)