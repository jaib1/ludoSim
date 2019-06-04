import numpy as np

class Board(): 
    """
    A class which represents a ludo board and runs the game of ludo.
    
    Attributes:
        numPlayers: The number of players in the game (max of 4)
        players: array of Player objects
      	numPieces: The number of ludo pieces for each player
      	pieces: array of Piece objects
      	piecePositions: NumPlayers * NumPieces array with int value of each position
      	scores: NumPlayers array with the current score for each player
      	homeArmSpaces: the length in spaces of each player's home arm
      	widthSpaces: the width in spaces between adjacent players
      	boardSpaces: the total number of spaces on the board
      	winner: the winner of the game
    """
    
    # define and limit attributes
    __slots__ = 'numPlayers', 'players', 'numPieces', 'pieces', \
        'piecePositions', 'scores', 'homeArmSpaces', 'widthSpaces', \
        'boardSpaces', 'winner'
    
    def __init__(self, numPlayers=2, numPieces=4, homeArmSpaces=6, 
                 widthSpaces=3):
        """
        The constructor requires the number of players, number of pieces, 
        number of board spaces in the home arm, and number of board spaces
        between adjacent players
        
        Parameters
        -----------
        (all parameters are self-descriptive)
        
        Examples
        --------
        b = Board()
        
        b = Board(numPlayers=4)
        
        b = Board(4,5,8,4)
        
        """
        
        self.numPlayers = numPlayers
        self.numPieces = numPieces
        self.homeArmSpaces = homeArmSpaces
        self.widthSpaces = widthSpaces
        
    # set private attributes:
    
    def playGame(self):
        """
        Starts and runs the game of ludo.
        """
    
    def updateBoard(self):
        """
        Updates the game board (`piecePositions`) after each move.
        """
    
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
        
        property
        
        