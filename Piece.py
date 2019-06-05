import numpy as np

class Piece(): 
    """
    A class which represents a player's piece in a ludo game. Instantiated and used by `Board`.
    
    Attributes:
    -----------
        __playerID: the ID of the player the piece belongs to
        __startPos: The board space number associated with the board space a 
          player's piece starts on upon leaving the home base with a roll of 6.
      	__scoreBasePos: The board space number associated with the last board 
          space a player's piece is on before entering the score arm.
        __boardPos: the current board space the piece occupies
        __scoreArmPos: the current score arm space the piece occupies
        __moveCount: the current number of spaces the piece has moved
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = '__playerID', '__boardPos', '__scoreArmPos', '__moveCount'
        
    def __init__(self, playerID):
        """
        The constructor requires the id of the player the piece belongs to.
        
        Parameters
        -----------
        playerID
        
        Examples
        --------
        p = Piece(1)
        
        """
        
        self.__playerID = playerID