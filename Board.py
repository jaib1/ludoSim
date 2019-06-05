import numpy as np
from ludoSim import Player # import other classes in this package

class Board(): 
    """
    A class which represents a ludo board and runs the game of ludo.

    Notes for clarification:
    ------------------------
        - Terminology:
            - "home base": The area a player's pieces occupy at game start
            - "score base": The area a player's pieces occupy upon a score
            - "score arm": The area on the board leading directly to the score 
                base. A player's pieces are "safe" when in this area.
            - "start position": The board space a player's piece occupies
            upon moving out of their home base. 
        - Board Space Numbering: The start position of player1 is considered 
        space 1. 
    
    Rules:
    ------
        - If a 6 is rolled: 
            1) A player may move a piece out of their home base
            and onto the board 
            2) The player rolls again
        - If a player's (e.g. player1) piece moves to the same board space 
        another player's (e.g. player2) piece occupies, the other player's 
        (player2) piece moves back to their home base
        - If a player's piece moves to a board space which another piece of
        the same player occupies, that space is now "blocked", and other
        players cannot move their pieces past that space
    
    Attributes:
    -----------
        __players: Array of Player objects
      	__piecePositions: NumPlayers * NumPieces array with int value of each 
          position
      	__scores: NumPlayers array with the current score for each player
      	__boardSpaces: The total number of spaces on the board
        __spacesBeforeScoreArm: The number of spaces a player's piece needs to
          move before entering the score arm.
      	__winner: The winner of the game
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = '__players', '__piecePositions', '__scores', '__boardSpaces', \
        '__winner'
    
    def __init__(self, numPlayers=2, numPieces=4, scoreArmSpaces=6, 
                 widthSpaces=3):
        """
        The constructor requires the number of players, number of pieces, 
        number of board spaces in the home arm, and number of board spaces
        between adjacent players. Based on these parameters, the constructor 
        initializes the `boardSpaces`, `players`. `piecePositions` and `scores` 
        attributes.
        
        Parameters
        -----------
        numPlayers
        numPieces
        scoreArmSpaces
        widthSpaces
        
        Examples
        --------
        b = Board()
        
        b = Board(numPlayers=4)
        
        b = Board(4,5,8,4)
        
        """
        
        self.__boardSpaces = (scoreArmSpaces+1)*8 + (widthSpaces-2)*4
        
        # build `players` array with comprehension
        self.__players = [Player(i,numPieces) for i in range(0,numPlayers)]
        
    
    def playGame(self):
        """
        Starts and runs the game of ludo.
        """
        
        # while isempty(winner):
        #   player.rollDie()
        #   player.makeMove()
        #   self.updateBoard()
    
    def updateBoard(self):
        """
        Updates the game board (`piecePositions`) after each move.
        """
        
        # update self.piecePositions
        # if any Piece.HomePos == scoreArmSpaces:
        #   Piece.HomePos +=1 
        #   self.updateScore()
    
    def updateScore(self):
        """
        Updates the game score (`scores`) any time a piece reaches the home 
        base.
        """
        
        if np.any(self.scores == self.numPieces): 
            self.endGame()
    
    def endGame(self):
        """
        Ends the game and declares a `winner` when a player has moved all of 
        their pieces to the home base.
        """
        print('endGame')
        
        