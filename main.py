from flask import Flask, render_template, redirect, url_for, session
from random import choice

app = Flask(__name__)
app.secret_key = 'group1'

class Game:
    def __init__(self):
        self.total_wins = 0
        self.total_losses = 0
        self.options = ['rock', 'paper', 'scissors', 'bomb']

    def set_player_choice(self, player_choice):
        return player_choice

    def set_computer_choice(self):
        return choice(self.options)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "draw"
        if (player_choice == 'rock' and computer_choice in ['scissors', 'bomb']) or \
           (player_choice == 'paper' and computer_choice in ['rock', 'bomb']) or \
           (player_choice == 'scissors' and computer_choice == 'paper') or \
           (player_choice == 'bomb' and computer_choice != 'bomb'):
            self.total_wins += 1
            return "win"
        else:
            self.total_losses += 1
            return "loss"

# Initialize the game instance
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/play/<choice>')
def play_game(choice):
    player_choice = game.set_player_choice(choice)
    computer_choice = game.set_computer_choice()

    result = game.determine_winner(player_choice, computer_choice)

    session['player_choice'] = player_choice
    session['computer_choice'] = computer_choice
    session['wins'] = game.total_wins
    session['losses'] = game.total_losses

    return redirect(url_for('results'))

@app.route('/results')
def results():
    player_choice = session.get('player_choice')
    computer_choice = session.get('computer_choice')
    wins = session.get('wins')
    losses = session.get('losses')

    return render_template('results.html', player_choice=player_choice, computer_choice=computer_choice, wins=wins, losses=losses)

if __name__ == '__main__':
    app.run(debug=True)
