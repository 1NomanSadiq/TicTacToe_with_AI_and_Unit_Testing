from model.Winner import Winner
from view.Show import Show
from controller.SaveAndLoad import SaveAndLoad
class Board:
    def __init__(self):
        self.gameOver = False
        self.gameBoard = {1: '-', 2: '-', 3: '-',
            4: '-', 5: '-', 6: '-',
            7: '-', 8: '-', 9: '-'}
        self.emptyGameBoard = {1: '-', 2: '-', 3: '-',
                    4: '-', 5: '-', 6: '-',
                    7: '-', 8: '-', 9: '-'}

    def updateGameBoard(self, player, position):
        winner = Winner()
        self.gameBoard[position] = player
        if(winner.getWinner(self.gameBoard) == 'X'):
            show = Show()
            show.printGameBoard(self.gameBoard)
            print("X Won!\n")
            SaveAndLoad.saveGame(self.emptyGameBoard)
            self.gameOver = True
        elif(winner.getWinner(self.gameBoard) == 'O'):
            show = Show()
            show.printGameBoard(self.gameBoard)
            print("O Won!\n")
            SaveAndLoad.saveGame(self.emptyGameBoard)
            self.gameOver = True
        elif(winner.isDraw(self.gameBoard)):
            show = Show()
            show.printGameBoard(self.gameBoard)
            SaveAndLoad.saveGame(self.emptyGameBoard)
            print("It's a Draw!\n")
            self.gameOver = True

    def validMove(self, position):
        if(self.gameBoard[position]=="-"):
            return True
        else:
            return False
    def getGameBoard(self):
        return self.gameBoard
    def setGameBoard(self, gameBoard):
        self.gameBoard = gameBoard

    def setMove(self, player, position):
        if(player == 'O' or player == 'X' or player == '-'):
            for key in range(1, 10):
                if key == position:
                    self.gameBoard[position] = player