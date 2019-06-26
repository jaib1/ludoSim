from ludoSim import * # import other classes in this analysis
from ludoSim.Piece import Piece
import numpy as np
import random
import collections

class Player():
    """
    A class which represents a player in a ludo game. Instantiated and used by 
    `Board`.
    
    Attributes:
        __board: The Board object which is the Player's parent
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
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = ('__board', '__id', '__startPos', '__scoreBasePos', '__pieces', 
        '__homePieces', '__activePieces', '__scorePieces', '__score')
        
    def __init__(self, board, id, startPos):
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
        b = Board()
        p = Player(b, 0, 0)
        
        """
        
        self.__board = board
        self.__id = id
        self.__startPos = startPos
        numPieces = self.__board._Board__numPieces
        # build `pieces` array with comprehension
        self.__pieces = [Piece(id, i) for i in range(0,numPieces)]
        self.__homePieces = self.__pieces
        #self.__homePieces = [Piece(id, i) for i in range(0,numPieces)]
        self.__activePieces = [] 
        self.__scorePieces = []
        self.__score = 0
        
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
                # update that piece's move count
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
        
        # create dict subsets? e.g., dicts for `ourPosns`, `othersPosns`,
        # `ourActivePiecePosns`,...
        
        # get necessary info from board
        allPiecePosns = self.__board._Board__piecePositions
        boardSpaces = self.__board._Board__boardSpaces
        scoreArmSpaces = self.__board._Board__scoreArmSpaces
        
        # get positions of all other pieces
        othersPosns = [allPiecePosns[key] for key in allPiecePosns.keys()
                      if not(key[0] == self.__id)]
        
        # out of all possible moves, get `pieceToMove`:
        
        pieceToMove = []
        
        # get our active piece numbers
        activePieceNums = [self.__activePieces[i]._Piece__pieceNum 
                          for i in range(0, len(self.__activePieces))]
        # get our potential positions
        rollPosns = [self.__pieces[piece]._Piece__boardPos + roll
                    for piece in activePieceNums]
        # get our potential move counts
        rollMoveCounts = [self.__pieces[piece]._Piece__moveCount + roll 
                         for piece in activePieceNums]
        # get our potential score arm positions
        rollScoreArmPosns = [self.__pieces[piece]._Piece__scoreArmPos + roll
                            for piece in activePieceNums]
        
        # get our potential positions
#        activePieceNums, rollPosns = map(list, zip(
#                              *[[self.__activePieces[piece]._Piece__pieceNum, 
#                              self.__activePieces[piece]._Piece__boardPos + roll] 
#                              for piece in range(0, len(self.__activePieces))]))
        
        # check to see if we can hit another piece
        canHitPos = [pos for pos in rollPosns if pos in othersPosns]
        
        # check to see if we can move in score arm
        canMoveInScoreArm = [activePieceNums[piece] for piece in range(0, len(activePieceNums)) 
                            if rollMoveCounts[piece] >= boardSpaces # if we are in score arm
                            and rollScoreArmPosns <= scoreArmSpaces] # and our move wouldn't be past score arm
        
        # check to see if there are any blocks:
        blockPosns = [pos for pos, count 
                     in collections.Counter(othersPosns).items() if count > 1]
                    
        # if, elif, elif, else block for 1) hitting another piece, 2) moving up
        # in score arm, 3) not moving past a block, 4) random move
        if canHitPos:
            pieceToMove = activePieceNums[rollPosns.index(canHitPos[0])]
        elif canMoveInScoreArm: # if we have a piece in score arm, move it, else check for blocks
            pieceToMove = canMoveInScoreArm[0]
        elif blockPosns:    
            piecesToMove = [piece for piece 
                           in range(0, len(self.__activePieces)) 
                           for block in blockPosns
                           if (rollPosns[piece] < blockPosns(block))]
            
            if piecesToMove:                  
                pieceToMove = random.choice(piecesToMove)
                
        else: # make sure the available pieces are not stuck in score arm
            piecesToMove = [pieceNum for pieceNum in activePieceNums
                           if activePieceNums[pieceNum] not in canMoveInScoreArm]
            
            if piecesToMove:                  
                pieceToMove = random.choice(piecesToMove)

        # if no possible moves, return
        if not(pieceToMove):
            return
        
        self.updateGame(roll, pieceToMove)
            
    def updateGame(self, roll, pieceToMove):
        # the move: update player '__score' and '__scorePieces'; 
        # piece `__moveCount`, `__boardPos`, `__scoreArmPos`;
        # and board `__piecePositions` and `__score`
        
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
        