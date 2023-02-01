class Winner:
    def checkWinner(self, gameBoard):
        if (gameBoard[1] == gameBoard[2] and gameBoard[1] == gameBoard[3] and gameBoard[1] != '-'):
            return gameBoard[1]
        elif (gameBoard[4] == gameBoard[5] and gameBoard[4] == gameBoard[6] and gameBoard[4] != '-'):
            return gameBoard[4]
        elif (gameBoard[7] == gameBoard[8] and gameBoard[7] == gameBoard[9] and gameBoard[7] != '-'):
            return gameBoard[7]
        elif (gameBoard[1] == gameBoard[4] and gameBoard[1] == gameBoard[7] and gameBoard[1] != '-'):
            return gameBoard[1]
        elif (gameBoard[2] == gameBoard[5] and gameBoard[2] == gameBoard[8] and gameBoard[2] != '-'):
            return gameBoard[2]
        elif (gameBoard[3] == gameBoard[6] and gameBoard[3] == gameBoard[9] and gameBoard[3] != '-'):
            return gameBoard[3]
        elif (gameBoard[1] == gameBoard[5] and gameBoard[1] == gameBoard[9] and gameBoard[1] != '-'):
            return gameBoard[1]
        elif (gameBoard[7] == gameBoard[5] and gameBoard[7] == gameBoard[3] and gameBoard[7] != '-'):
            return gameBoard[7]
        else:
            return "None"

    def getWinner(self, gameBoard):
        return self.checkWinner(gameBoard)

    def isDraw(self, gameBoard):
        for key in gameBoard.keys():
            if (gameBoard[key] == '-'):
                return False
        return True
