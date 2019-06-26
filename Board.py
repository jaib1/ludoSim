from ludoSim import * # import other classes in this package
from ludoSim.Player import Player
import numpy as np


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
          space 0. 
    
    Rules:
    ------
        - If a 6 is rolled: 
            1) A player may move a piece out of their home base
            and onto the board 
            2) The player rolls again
        - If a player's (e.g. player0) piece moves to the same board space 
        another player's (e.g. player1) piece occupies, the other player's 
        (player1) piece moves back to their home base
        - If a player's piece moves to a board space which another piece of
        the same player occupies, that space is now "blocked", and other
        players cannot move their pieces past that space
    
    Attributes:
    -----------
        __players: Array of Player objects
      	__piecePosns: dict of piece positions [PlayerIDPieceId:PiecePos] of 
          NumPlayers * NumPieces length
        __startPosns: an array with the start position for each player
      	__scores: NumPlayers array with the current score for each player
      	__boardSpaces: The total number of spaces on the board
        __scoreArmSpaces: The number of spaces a player's piece needs to
          move before entering the score arm.
      	__winner: The winner of the game
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = ('__players', '__piecePosns', '__startPosns', 
        '__scores', '__boardSpaces', '__spacesArray', '__winner', 
        '__numPlayers', '__numPieces', '__scoreArmSpaces', '__widthSpaces')
    
    def __init__(self, numPlayers=2, numPieces=4, scoreArmSpaces=5, 
                 widthSpaces=3):
        """
        The constructor requires the number of players, number of pieces, 
        number of board spaces in the home arm, and number of board spaces
        between adjacent players. Based on these parameters, the constructor 
        initializes the `__boardSpaces`, `__spacesArray`, `__players`, 
        `__piecePositions` and `__scores` attributes.
        
        Parameters
        ----------
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
        
        # dict of piece positions: {"playerID""pieceNum": boardPos}
        self.__piecePosns = {str(player)+str(piece):-1000 
                                for player in range(0,numPlayers) 
                                for piece in range(0,numPieces)}
        self.__scores = [0 for i in range(0,numPlayers)] 
        self.__numPlayers = numPlayers 
        self.__numPieces = numPieces 
        self.__scoreArmSpaces = scoreArmSpaces 
        self.__widthSpaces = widthSpaces
        self.__boardSpaces = (scoreArmSpaces+1)*8 + (widthSpaces-2)*4
        # build `__startPositions` array
        self.__startPosns = [(i * (2*(scoreArmSpaces+1)+1)) 
                                for i in range(0,numPlayers)]
        # build `__players` array
        self.__players = [Player(self, i, self.__startPosns[i]) 
                         for i in range(0,numPlayers)]
        self.__winner = []
         
    def playGame(self):
        """
        Starts and runs the game of ludo.
        """
        turnNumber = 0
        
        while not(self.__winner):
            # roll die
            roll = np.random.randint(1,7)
        
            # player makes move
            playerTurn = turnNumber % self.__numPlayers
            self.__players[playerTurn].makeMove(roll)
            if not(roll == 6):
                turnNumber +=1 
            
            self.updateScore()
    
    def updateScore(self):
        """
        Updates the game score (`scores`) any time a piece reaches the home 
        base.
        """
        
        if np.any(self.__scores == self.__numPieces): 
            self.endGame()
    
    def endGame(self):
        """
        Ends the game and declares a `winner` when a player has moved all of 
        their pieces to the home base.
        """
        self.__winner = [player for player in range(0, len(self.__players))
                        if self.__scores[player] == self.__numPieces]
        
        print('Game over. Player %s wins' % self.__winner)
        
        