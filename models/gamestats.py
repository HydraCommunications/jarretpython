class GameStats:
    def __init__(self, wins, losses, options, playerChoice, ComputerChoice):
        self.wins = wins
        self.losses = losses
        self.options = options
        self.playerChoice = playerChoice
        self.ComputerChoice = ComputerChoice

    def setComputerChoice(self, ComputerChoice):
       if ComputerChoice == 1:
           choice = " "
       if ComputerChoice == 2:
           choice = " "
       if ComputerChoice == 3:
           choice = " "
       if ComputerChoice == 4:
           choice = " "

    def setPlayerChoice(self, playerChoice):
        if playerChoice == 1:
            choice = " "
        if playerChoice == 2:
            choice = " "
        if playerChoice == 3:
            choice = " "
        if playerChoice == 4:
            choice = " "