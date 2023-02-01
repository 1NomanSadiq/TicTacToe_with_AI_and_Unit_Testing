import os
class SaveAndLoad:
        @staticmethod
        def saveGame(gameBoard):
            with open("saved.txt", "w") as file:
                for x in gameBoard.keys():
                    file.write(str(x) + " " + gameBoard[x]+ "\n")
                file.close
        @staticmethod
        def loadGame(gameBoard):
            if not os.path.exists("./saved.txt"):
                SaveAndLoad.saveGame(gameBoard)
            with open("saved.txt", "r") as file:
                for lines in file:
                    (key, val) = lines.split()
                    gameBoard[int(key)] = val
                file.close()
