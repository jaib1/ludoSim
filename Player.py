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
        __boardSpaces: see `Board.__boardSpaces`
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = ('__id', '__startPos', '__scoreBasePos', '__pieces', 
        '__homePieces', '__activePieces', '__scorePieces', '__score', 
        '__spacesArray')
        
    def __init__(self, id, numPieces, startPos, boardSpaces):
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
        self.__score = 0
        self.__boardSpaces = boardSpaces
#        self.__spacesArray = spacesArray
    
    def makeMove(self, roll):
        """
        Takes a simulated die roll and subsequently moves a piece, if
        possible, for the player.
        
        Parameters
        ----------
        roll: a simulated die roll
        
        Examples
        --------
        roll = np.random.randint(1,7)
        p.makeMove(roll)
        
        p.makeMove(6)   
        """
        
        # special case if roll == 6
        if roll == 6:
            
            # if no pieces in play
            if not(self.__activePieces): 
                # move a piece out from home base and get its piece num
                self.__activePieces.append(self.__homePieces.pop())
#                pieceNum = self.__activePieces[-1].__pieceNum
                # move that piece to the start position
                self.__activePieces[-1].__boardPos = self.__startPos
#                self.__pieces[pieceNum].__boardPos = self.__startPos
                # update that pieces move count
                self.__activePieces[-1].__moveCount = 1
#                self.__pieces[pieceNum].__moveCount = 1 
            else:
                self.moveHeuristic(roll)
        
        else:         
            if not(self.__activePieces): # if no pieces in play 
                return 
            else: # if active pieces
                self.moveHeuristic(roll)

    
    def moveHeuristic(self, roll):
        """
        Uses heuristics to pick which piece to move, based on trying to hit
        another player's piece, and not moving within a die roll of another 
        player's piece
        """
        
        # check to see which pieces CAN move
        posMoves = len(self.__activePieces) - 1
        
        # label the possible moves, get `pieceToMove`
        pieceToMove = []
        while posMoves >= 0:
            
            # check to see if we can hit another piece
            ourPos = self.__activePieces(posMoves).__boardPos
            othersPos = 

            posMoves -= 1
        
        # if no possible moves, return
        if not(pieceToMove):
            return
        # the move: update piece `__moveCount`, `__boardPos`, `__scoreArmPos`
        self.__pieces[pieceToMove].__moveCount += roll
        self.__pieces[pieceToMove].__boardPos = ( 
            (self.__startPos + self.__pieces[pieceToMove].__moveCount) 
            % self.__boardSpaces) 
        # if we are in the score arm...
        if self.__pieces[pieceToMove].__moveCount > self.__boardSpaces:
            # update `__scoreArmPos`
            self.__pieces[pieceToMove].__scoreArmPos = (
                    self.__pieces[pieceToMove].__moveCount - self.__boardSpaces)
            # remove piece from board
            self.__pieces[pieceToMove].__boardPos = 0
            
        