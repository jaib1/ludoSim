from ludoSim import * # import other classes in this analysis
from ludoSim.Piece import Piece
import numpy as np
import random
import collections

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
        __piecePositions: see `Board.__piecePositions`
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = ('__id', '__startPos', '__scoreBasePos', '__pieces', 
        '__homePieces', '__activePieces', '__scorePieces', '__score', 
        '__spacesArray', '__boardSpaces', '__piecePositions')
        
    def __init__(self, id, numPieces, startPos, boardSpaces, piecePositions):
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
        p = Player(1,4,1,50,[0,0,0,0])
        
        p = Player(startPos=14, boardSpaces=50, piecePositions=[0,0,0,0], numPieces=5, id=2)      
        """
        
        self.__id = id
        self.__startPos = startPos
        # build `pieces` array with comprehension
        self.__pieces = [Piece(id, i) for i in range(0,numPieces)]
        self.__homePieces = [Piece(id, i) for i in range(0,numPieces)]
        self.__activePieces = [] 
        self.__scorePieces = []
        self.__score = 0
        self.__boardSpaces = boardSpaces
        self.__piecePositions = piecePositions;
#        self.__spacesArray = spacesArray
        
    def __iter__(self):
        """
        Generator Function to use class as iterator.
        """
    
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
                # move that piece to the start position
                self.__activePieces[-1]._Piece__boardPos = self.__startPos
                # update that pieces move count
                self.__activePieces[-1]._Piece__moveCount = 1
            else:
                self.moveHeuristic(roll)
        
        else:         
            if not(self.__activePieces): # if no pieces in play 
                return 
            else: # if active pieces
                self.moveHeuristic(roll)

    
    def moveHeuristic(self, roll):
        """
        Uses heuristics to pick which piece to move, based on 1) trying to hit
        another player's piece, 2) not moving within a die roll of another 
        player's piece, 3) moving up in the score arm, and 4) not moving past a 
        block
        
        Parameters
        ----------
        roll: a simulated die roll
        
        Examples
        --------
        roll = np.random.randint(1,7)
        p.moveHeuristic(roll)
        
        p.moveHeuristic(6)   
        """
        
        # get positions of all other pieces
        othersPosns = [self.__piecePositions[pr][1] for pr
                    in range(0, len(self.__piecePositions)) 
                    if self.__piecePositions[pr][0] != self.__id
                    & self.__piecePositions[pr][1] != -1000]
        
        # out of all possible moves, get `pieceToMove`:
        
        pieceToMove = []
        
        # get our pieces, and our potential positions
        ourPieceNums, ourRollPosns = map(list, zip(
                              *[[self.__activePieces[piece]._Piece__pieceNum, 
                              self.__activePieces[piece]._Piece__boardPos + roll] 
                              for piece in range(0, len(self.__activePieces))]))
        
        # check to see if we can hit another piece
        canHit = [pos for pos in ourRollPosns if pos in othersPosns]
        
        # check to see if we can move in score arm
        canMoveInScoreArm = [piece for piece in range(0, len(ourPieceNums)) 
                            if (self.__pieces[piece]._Piece.__moveCount > self.__boardSpaces) # if we are in score arm
                            and 
                            ((self.__pieces[piece].__Piece__scoreArmPos + roll) 
                            < self.__scoreArmSpaces)] # and our move wouldn't be past score arm
        
        # check to see if there are any blocks:
        blockPosns = [piece for piece, count 
                     in collections.Counter(othersPosns).items() if count > 1]
                    
        # if, elif, else block for 1) hitting another piece, 2) moving up in
        # score arm, 3) not moving past a block
        if canHit:
            pieceToMove = ourPieceNums[ourRollPosns.index(canHit[0])]
        elif canMoveInScoreArm: # if we have a piece in score arm, move it, else check for blocks
            pieceToMove = canMoveInScoreArm[0]
        elif blockPosns:    
            piecesToMove = [piece for piece 
                           in range(0, len(self.__activePieces)) 
                           for block in blockPosns
                           if (ourRollPosns[piece] < blockPosns(block))]
            
            if piecesToMove:                  
                pieceToMove = random.choice(piecesToMove)
                
        else: # make sure the available pieces are not stuck in score arm
            piecesToMove = [pieceNum for pieceNum in ourPieceNums
                           if ourPieceNums[pieceNum] not in canMoveInScoreArm]
            
            if piecesToMove:                  
                pieceToMove = random.choice(piecesToMove)

        # if no possible moves, return
        if not(pieceToMove):
            return
        
        # the move: update piece `__moveCount`, `__boardPos`, `__scoreArmPos`
        self.__pieces[pieceToMove]._Piece__moveCount += roll
        self.__pieces[pieceToMove]._Piece__boardPos = ( 
            (self.__startPos + self.__pieces[pieceToMove]._Piece__moveCount) 
            % self.__boardSpaces) 
        # if we are in the score arm...
        if self.__pieces[pieceToMove]._Piece__moveCount > self.__boardSpaces:
            # update `__scoreArmPos`
            self.__pieces[pieceToMove]._Piece__scoreArmPos = (
                self.__pieces[pieceToMove]._Piece__moveCount - self.__boardSpaces)
            # remove piece from board
            self.__pieces[pieceToMove]._Piece__boardPos = -1000
            
        