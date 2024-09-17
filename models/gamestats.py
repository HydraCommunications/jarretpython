class GameStats:
    def __init__(self, wins, losses, options, playerChoice, ComputerChoice):
        self.wins = wins
        self.losses = losses
        self.options = options
        self.playerChoice = playerChoice
        self.ComputerChoice = ComputerChoice

    def setComputerChoice(self, ComputerChoice):
       if ComputerChoice == 1:
           choice = "/static/paper.jpg"
       if ComputerChoice == 2:
           choice = "/static/rock.jpg"
       if ComputerChoice == 3:
           choice = "/static/scissors.jpg"
       if ComputerChoice == 4:
           choice = " "

    def setPlayerChoice(self, playerChoice):
        if playerChoice == 1:
            choice = "/static/paper.jpg"
        if playerChoice == 2:
            choice = "/static/rock.jpg"
        if playerChoice == 3:
            choice = "/static/scissors.jpg"
        if playerChoice == 4:
            choice = " "