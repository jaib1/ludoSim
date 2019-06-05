import numpy as np
from ludoSim import Piece

class Player():
    """
    A class which represents a player in a ludo game. Instantiated and used by `Board`.
    
    Attributes:
        __homeBase: The home base (of the four possible bases) of the player.
            The home base serves as the player's ID, and designates the
            player's start position and score base position in terms of the
            board space numberings.
        __startPos: The board space number associated with the board space a 
          player's piece starts on upon leaving the home base with a roll of 6.
      	__scoreBasePos: The board space number associated with the last board 
          space a player's piece is on before entering the score arm.
      	__pieces: Array of Piece objects
      	____homePieces: The player's pieces currently in the their home base
      	__activePieces: The player's pieces currently on the ludo board
      	__scorePieces: The player's pieces currently in their score base
      	__score: The player's current score
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = '__homeBase', '__startPos', '__scoreBasePos', '__pieces', \
        '__homePieces', '__activePieces', '__scorePieces', '__score'
        
    def __init__(self, homeBase, numPieces):
        """
        The constructor requires the home base position, and the number of 
        pieces.
        
        Parameters
        -----------
        homeBase
        numPieces
        
        Examples
        --------
        p = Player(1,4)
        
        p = Player(numPieces=5, homeBase=2)
        
        """
        
        self.__homeBase = homeBase