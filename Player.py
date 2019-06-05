import numpy as np
from ludoSim import Piece

class Player():
    """
    A class which represents a player in a ludo game. Instantiated and used by `Board`.
    
    Attributes:
        __id: The home base (of the four possible bases) of the player.
            The home base serves as the player's ID, and designates the
            player's start position and score base position in terms of the
            board space numberings.
        __startPos: The board space number associated with the board space a 
          player's piece starts on upon leaving the home base with a roll of 6.
      	__pieces: Array of Piece objects
      	__homePieces: The player's pieces currently in the their home base
      	__activePieces: The player's pieces currently on the ludo board
      	__scorePieces: The player's pieces currently in their score base
      	__score: The player's current score
        __spacesArray: see Board.__spacesArray
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = '__id', '__startPos', '__scoreBasePos', '__pieces', \
        '__homePieces', '__activePieces', '__scorePieces', '__score', \
        '__spacesArray'
        
    def __init__(self, id, numPieces, startPos, spacesArray):
        """
        The constructor requires the home base position, the number of 
        pieces, and the start position upon leaving the home base on a roll of 
        6. Based on these parameters, the constructor initializes the
        `__id`, `__startPos`, `__pieces`, and `__homePieces` attributes. 
        
        Parameters
        -----------
        id
        numPieces
        
        Examples
        --------
        p = Player(1,4,1)
        
        p = Player(startPos=14, numPieces=5, id=2)
        
        """
        
        self.__id = id
        self.__startPos = startPos
        # build `pieces` array with comprehension
        self.__pieces = [Piece(id,i) for i in range(0,numPieces)]
        self.__homePieces = self.__pieces
        self.__activePieces = [] 
        self.__scorePieces = []
        self.__spacesArray = spacesArray
    
    def makeMove(self, roll):
        """
        `makeMove` takes a simulated dice roll and subsequently moves a piece,
        if possible, for the player.
        
        """
        # make move
        if roll == 6:
            # if no pieces in play
            if not(self.__activePieces): 
                # move a piece out from home base
                self.__activePieces.append(self.__homePieces[-1].pop())
                # move that piece to the start position
                self.__pieces[self.__activePieces[-1].pieceNum]._Piece.__boardPos = self.__startPos
                
        else:
            if not(self.__activePieces): # if no pieces in play 
                return 
            else:
        
        # if our new val is greater than the number of board spaces, loop
        # around to board space 1. have move count. then relative val.
                
        # newPosVal = self.__pieces[pieceToMove].__boardPos += roll
        # self.__pieces[pieceToMove].__boardPos = self.__spacesArray[newPosVal]
        