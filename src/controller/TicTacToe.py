from controller.SaveAndLoad import SaveAndLoad
from model.Board import Board
from model.Winner import Winner
from controller.AI import AI
from view.Show import Show
from collections import Counter
class TicTacToe:
    def __init__(self):
        self.show = Show()
        self.winner = Winner()
        self.theAi = AI()
        self.board = Board()
        self.player = 'O'
        self.ai = 'X'
        self.emptyGameBoard = {1: '-', 2: '-', 3: '-',
                     4: '-', 5: '-', 6: '-',
                     7: '-', 8: '-', 9: '-'}

    def playerOMove(self):
        while True:
            while True:
                try:
                    position = int(input("Player O Choose your move (1-9): "))
                    if(self.board.validMove(position)):
                        return position
                except ValueError:
                    print("Invalid Input")

    def playerXMove(self):
        while True:
            while True:
                try:
                    position = int(input("Player X Choose your move (1-9): "))
                    if(self.board.validMove(position)):
                        return position
                except ValueError:
                    print("Invalid Input")

    def startGame(self):

        choice = None
        aiMode = False

        while not (choice == 'y' or choice == 'Y' or choice == 'n' or choice == 'N'):
            choice = input("Do you want to play AI Mode? (y/n):")
            if(choice == 'y' or choice == 'Y'):
                aiMode = True

        choice = None
        while not (choice == 'y' or choice == 'Y' or choice == 'n' or choice == 'N'):
            choice = input("Do you want to load the game if saved? (y/n):")
            if(choice == 'y' or choice == 'Y'):
                SaveAndLoad.loadGame(self.board.getGameBoard())

        self.player = 'O'
        self.ai = 'X'

        gameLoaded = True
        if Counter(self.board.getGameBoard().values())['X'] > Counter(self.board.getGameBoard().values())['O']:
            self.player = 'O'
        
        self.show.printGameBoard(self.board.getGameBoard())

        if (self.board.getGameBoard() == self.emptyGameBoard):
            gameLoaded = False

        if(not gameLoaded and aiMode):
            print("Unbeatable AI goes first...")
        while True:
            if(aiMode):
                if not gameLoaded:
                    move = self.theAi.getAiMove(self.board.getGameBoard(), self.player, self.ai)
                    self.board.updateGameBoard(self.ai, move)
                    if(self.board.gameOver):
                        break
                    self.show.printGameBoard(self.board.getGameBoard())
                    SaveAndLoad.saveGame(self.board.getGameBoard())
                move = self.playerOMove()
                self.board.updateGameBoard(self.player, move)
                gameLoaded = False
                if self.board.gameOver:
                    break
                self.show.printGameBoard(self.board.getGameBoard())
                SaveAndLoad.saveGame(self.board.getGameBoard())
            else:
                if(self.player == 'X'):
                    move = self.playerXMove()
                    self.board.updateGameBoard(self.player, move)
                    self.player = 'O'
                    if self.board.gameOver:
                        break
                    self.show.printGameBoard(self.board.getGameBoard())
                    SaveAndLoad.saveGame(self.board.getGameBoard())
                move = self.playerOMove()
                self.board.updateGameBoard(self.player, move)
                self.player = 'X'
                if self.board.gameOver:
                    break
                self.show.printGameBoard(self.board.getGameBoard())
                SaveAndLoad.saveGame(self.board.getGameBoard())