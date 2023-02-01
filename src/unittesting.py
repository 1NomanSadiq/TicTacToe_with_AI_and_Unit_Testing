import unittest
from controller.SaveAndLoad import SaveAndLoad
from controller.TicTacToe import TicTacToe
import os

class UnitTesting(unittest.TestCase):
    #when game starts
    def test_onGameLoad(self):
        t = TicTacToe()
        #check that game is not over
        self.assertEqual(t.board.gameOver, False)
        #check that board is empty
        self.assertEqual(t.board.getGameBoard(), t.emptyGameBoard)
        #check that winner is none
        self.assertEqual(t.winner.getWinner(t.board.gameBoard), "None")
        #check that first player is 'O'
        self.assertEqual(t.player, 'O')
        #check that empty board is really empty
        emptyGameBoard = {1: '-', 2: '-', 3: '-',
                     4: '-', 5: '-', 6: '-',
                     7: '-', 8: '-', 9: '-'}
        self.assertEqual(t.emptyGameBoard, emptyGameBoard)

    def test_not_empty_after_making_a_move(self):
        t = TicTacToe()
        t.board.setMove('X', 5)
        emptyGameBoard = {1: '-', 2: '-', 3: '-',
                     4: '-', 5: '-', 6: '-',
                     7: '-', 8: '-', 9: '-'}
        self.assertNotEqual(t.board.getGameBoard(), emptyGameBoard)

    def test_playing_move_on_same_position_is_invalid(self):
        t = TicTacToe()
        t.board.setMove('X', 1)
        self.assertEqual(t.board.validMove(1), False)
        t.board.setMove('O', 2)
        self.assertEqual(t.board.validMove(2), False)

    def test_playing_move_on_different_position_is_valid(self):
        t = TicTacToe()
        t.board.setMove('X', 5)
        self.assertEqual(t.board.validMove(2), True)
        t.board.setMove('O', 3)
        self.assertEqual(t.board.validMove(4), True)

    def test_winner_is_none_when_board_is_empty(self):
        t = TicTacToe()
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "None")

    def test_winner_is_none_after_one_or_two_moves(self):
        t = TicTacToe()
        t.board.setMove('O', 1)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "None")
        t.board.setMove('O', 2)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "None")

    def test_many_moves_but_winner_is_none(self):
        t = TicTacToe()
        t.board.setMove('O', 1)
        t.board.setMove('X', 2)
        t.board.setMove('X', 3)
        t.board.setMove('O', 4)
        t.board.setMove('X', 7)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "None")

    def test_player_X_should_win_on_first_column(self):
        t = TicTacToe()
        t.board.setMove('X', 1)
        t.board.setMove('O', 2)
        t.board.setMove('X', 4)
        t.board.setMove('O', 5)
        t.board.setMove('X', 7)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_first_column(self):
        t = TicTacToe()
        t.board.setMove('O', 1)
        t.board.setMove('X', 2)
        t.board.setMove('O', 4)
        t.board.setMove('X', 5)
        t.board.setMove('O', 7)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_player_X_should_win_on_second_column(self):
        t = TicTacToe()
        t.board.setMove('X', 2)
        t.board.setMove('O', 3)
        t.board.setMove('X', 5)
        t.board.setMove('O', 6)
        t.board.setMove('X', 8)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_second_column(self):
        t = TicTacToe()
        t.board.setMove('O', 2)
        t.board.setMove('X', 3)
        t.board.setMove('O', 5)
        t.board.setMove('X', 6)
        t.board.setMove('O', 8)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_player_X_should_win_on_third_column(self):
        t = TicTacToe()
        t.board.setMove('X', 3)
        t.board.setMove('O', 4)
        t.board.setMove('X', 6)
        t.board.setMove('O', 7)
        t.board.setMove('X', 9)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_third_column(self):
        t = TicTacToe()
        t.board.setMove('O', 3)
        t.board.setMove('X', 4)
        t.board.setMove('O', 6)
        t.board.setMove('X', 7)
        t.board.setMove('O', 9)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_player_X_should_win_on_first_row(self):
        t = TicTacToe()
        t.board.setMove('X', 1)
        t.board.setMove('O', 4)
        t.board.setMove('X', 2)
        t.board.setMove('O', 7)
        t.board.setMove('X', 3)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_first_row(self):
        t = TicTacToe()
        t.board.setMove('O', 1)
        t.board.setMove('X', 4)
        t.board.setMove('O', 2)
        t.board.setMove('X', 7)
        t.board.setMove('O', 3)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_player_X_should_win_on_second_row(self):
        t = TicTacToe()
        t.board.setMove('X', 4)
        t.board.setMove('O', 1)
        t.board.setMove('X', 5)
        t.board.setMove('O', 7)
        t.board.setMove('X', 6)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_second_row(self):
        t = TicTacToe()
        t.board.setMove('O', 4)
        t.board.setMove('X', 1)
        t.board.setMove('O', 5)
        t.board.setMove('X', 7)
        t.board.setMove('O', 6)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_player_X_should_win_on_third_row(self):
        t = TicTacToe()
        t.board.setMove('X', 7)
        t.board.setMove('O', 4)
        t.board.setMove('X', 8)
        t.board.setMove('O', 5)
        t.board.setMove('X', 9)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_third_row(self):
        t = TicTacToe()
        t.board.setMove('O', 7)
        t.board.setMove('X', 4)
        t.board.setMove('O', 8)
        t.board.setMove('X', 5)
        t.board.setMove('O', 9)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_player_X_should_win_on_third_row(self):
        t = TicTacToe()
        t.board.setMove('X', 7)
        t.board.setMove('O', 4)
        t.board.setMove('X', 8)
        t.board.setMove('O', 5)
        t.board.setMove('X', 9)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_third_row(self):
        t = TicTacToe()
        t.board.setMove('O', 7)
        t.board.setMove('X', 4)
        t.board.setMove('O', 8)
        t.board.setMove('X', 5)
        t.board.setMove('O', 9)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_player_X_should_win_on_LTR_diagonal(self):
        t = TicTacToe()
        t.board.setMove('X', 1)
        t.board.setMove('O', 4)
        t.board.setMove('X', 5)
        t.board.setMove('O', 6)
        t.board.setMove('X', 9)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_LTR_diagonal(self):
        t = TicTacToe()
        t.board.setMove('O', 1)
        t.board.setMove('X', 4)
        t.board.setMove('O', 5)
        t.board.setMove('X', 6)
        t.board.setMove('O', 9)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_player_X_should_win_on_RTL_diagonal(self):
        t = TicTacToe()
        t.board.setMove('X', 3)
        t.board.setMove('O', 4)
        t.board.setMove('X', 5)
        t.board.setMove('O', 6)
        t.board.setMove('X', 7)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "X")

    def test_player_O_should_win_on_RTL_diagonal(self):
        t = TicTacToe()
        t.board.setMove('O', 3)
        t.board.setMove('X', 4)
        t.board.setMove('O', 5)
        t.board.setMove('X', 6)
        t.board.setMove('O', 7)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "O")

    def test_winner_should_be_a_none_when_no_move_left(self):
        t = TicTacToe()
        t.board.setMove('O', 1)
        t.board.setMove('X', 2)
        t.board.setMove('O', 4)
        t.board.setMove('X', 5)
        t.board.setMove('O', 8)
        t.board.setMove('X', 7)
        t.board.setMove('O', 9)
        t.board.setMove('X', 6)
        t.board.setMove('O', 3)
        self.assertEqual(t.winner.getWinner(t.board.getGameBoard()), "None")

    def test_game_saves_successfully(self):
        t = TicTacToe()
        SaveAndLoad.saveGame(t.board.getGameBoard())
        self.assertTrue(os.path.exists("./saved.txt"))

    def test_game_load_successfully(self):
        t = TicTacToe()
        t.board.setMove('O', 1)
        SaveAndLoad.saveGame(t.board.getGameBoard())
        #creating a new object so that the new board an empty board
        t = TicTacToe()
        self.assertEqual(t.board.getGameBoard(), t.board.emptyGameBoard)
        SaveAndLoad.loadGame(t.board.getGameBoard())
        self.assertEqual(t.board.gameBoard[1], 'O')

if __name__ == '__main__':
    unittest.main()