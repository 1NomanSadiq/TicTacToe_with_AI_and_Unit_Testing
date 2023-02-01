**Contents:**

1.  Introduction
2.  Architecture
3.  Serialization and Deserialization
4.  Game AI
5.  Tests
6.  Speed Up
7.  Conclusions and prospects
1.  **Introduction**

. Tic-Tac-Toe is a turn-based two-player puzzle game, traditionally played on a two-dimensional 3 × 3 grid. The active player alternates every round, where it places one marker on the board. The game is finished when either player is able to make a continuous horizontal, vertical or diagonal line on the 3 × 3 grid.

The project is divided in several packages. They are all called from the src module located at the root of the project. The src package provides class of the program to start the game. The model package contains Board, Player and Winner classes. View package contains Show class which displays the game on the screen using print function. Controller package contains the Controller class which is the core class of the game. It controls the game, takes the input from the user and communicates with other classes and SaveAndLoad class is responsible to save and load the game from a file in the local storage. Another module named “unittest.py” is added. It includes the unit testing of the working of the project; in case the game is misbehaving this file can be handy to maintain the game.

An AI is implemented using minimax algorithm which makes the AI unbeatable. You need to run Play.py residing in the src to start the game. You can run unittesting.py in the src to test the project.

1.  **Architecture**

![](media/995676140a5fef987bf9431d4b1a9f21.png)

1.  **Serialization and Deserialization**

When the game is being played all its values are stored in a dictionary. The occupied places are stored as X or O while unoccupied values are stores as a dash (-). Whenever a move is made by either of a player or AI the current state of game ie, the current state of the dictionary is stored in text file locally where each line a pair of key and value separated by a white space. Hence there are total of 9 lines in the text file. The saved text file is named “saved.txt”. And when the user enters the game the data from the local file is loaded into the dictionary and that way the game continues and restores its state. In case if the file does not exist it is created by the program automatically. It then has the data of an empty board such that each of the value is a dash (-). When the game is over ie the match is a draw or either X or O won the file is then again updated with an empty board.

1.  **Game AI**

The AI is made using minimax algorithm. Minimax is a strategy of always minimizing the maximum possible loss which can result from a choice that a player makes. The Mini-max algorithm is a repetitive algorithm used in decision-making and game theory. It gives a perfect move to a player who assumes that the enemy is also playing perfectly. The Mini-Max algorithm uses recursion to search the game tree.

The key to the Minimax algorithm is to go back and forth between two players, in which the "turning" player wishes to choose a move with a highest score. Next, the points for each available movement are determined by the opponent who decides which the available move has the lowest score.

1.  **Tests**

    Test cases are made in the code; unit testing is done using the python library unittest. The file can be run to test the game if it’s behaving as expected.

Testing was also done manually. Table is as follow.

| **Test Case** | **Condition**                            | **Expected Result**                   | **Actual Result**                     |
|---------------|------------------------------------------|---------------------------------------|---------------------------------------|
| 1             | Row 1 belongs to the X or O              | Player (X or O) Won! Game is finished | Player (X or O) Won! Game is finished |
| 2             | Row 2 belongs to X or O                  | Player (X or O) Won! Game is finished | Player (X or O) Won! Game is finished |
| 3             | Row 3 belongs to X or O                  | Player (X or O) Won! Game is finished | Player (X or O) Won! Game is finished |
| 4             | Column 1 belongs to X or O               | Player (X or O) Won! Game is finished | Player (X or O) Won! Game is finished |
| 5             | Column 2 belongs to X or O               | Player (X or O) Won! Game is finished | Player (X or O) Won! Game is finished |
| 6             | Column 3 belongs to X or O               | Player (X or O) Won! Game is finished | Player (X or O) Won! Game is finished |
| 8             | Left to Right Diagonal belongs to X or O | Player (X or O) Won! Game is finished | Player (X or O) Won! Game is finished |
| 9             | Right to Left Diagonal belongs to X or O | Player (X or O) Won! Game is finished | Player (X or O) Won! Game is finished |
| 10            | None of above but board is filled        | No one won, it’s a Draw!              | No one won, it’s a Draw!              |

Moreover, a few were played against AI and other player to make sure we reach 100% line coverage of our code. Game status is stored in file, the AI is unbeatable and everything worked as expected.

1.  **Speed Up**

cProfile was used for profiling the code and detecting the slow parts but could not a find a way to improve the slow parts. The minimax algorithm has a lot of iterations which makes the code slower. Performance could be improved using various methods such as alpha beta pruning. But we avoided using such methods to not increase the complexity of the code.

1.  **Conclusions and prospects**

The program is a Tic Tac Toe game on the command line for two players or a player and AI. The AI uses minimax algorithm and gives the optimal move which makes it impossible to beat. Two players can match with each other on choice. As the game processes it is stored in a text file locally and loaded when the game starts. Testing was done to make sure each part of the game is working perfectly.

The game/program could be further improved by using alpha beta pruning.
