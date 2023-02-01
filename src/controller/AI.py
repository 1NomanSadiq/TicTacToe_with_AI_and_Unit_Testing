from model.Winner import Winner
class AI:
    winner = Winner()
        
    def getAiMove(self, gameBoard, player, ai):
        bestScore = -1000
        bestMove = 0
        for key in gameBoard.keys():
            if (gameBoard[key] == '-'):
                gameBoard[key] = ai
                score = self.minimax(gameBoard, False, player, ai)
                gameBoard[key] = '-'
                if (score > bestScore):
                    bestScore = score
                    bestMove = key
        print("AI Move")
        return bestMove

    def minimax(self, gameBoard, isMaximizing, player, ai):
        if (self.winner.getWinner(gameBoard) == ai):
            return 100
        elif (self.winner.getWinner(gameBoard) == player):
            return -100
        elif (self.winner.isDraw(gameBoard)):
            return 0

        if (isMaximizing):
            bestScore = -1000
            for key in gameBoard.keys():
                if (gameBoard[key] == '-'):
                    gameBoard[key] = ai
                    score = self.minimax(gameBoard, False, player, ai)
                    gameBoard[key] = '-'
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = 1000
            for key in gameBoard.keys():
                if (gameBoard[key] == '-'):
                    gameBoard[key] = player
                    score = self.minimax(gameBoard, True, player, ai)
                    gameBoard[key] = '-'
                    if (score < bestScore):
                        bestScore = score
            return bestScore
