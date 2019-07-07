from ludoSim import * # import other classes in this analysis
from ludoSim.Piece import Piece
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
    __slots__ = ('__board', '__id', '__startPos', '__homePieces', 
                 '__activePieces', '__scorePieces', '__score')
        
    def __init__(self, board, id, startPos):
        """
        The constructor requires the home base position, the number of 
        pieces, and the start position upon leaving the home base on a roll of 
        6. Based on these parameters, the constructor initializes the
        `__id`, `__startPos`, `__pieces`, and `__homePieces` attributes. 
        
        Parameters
        -----------
        board
        id
        startPos
        
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
        self.__homePieces = [Piece(id, i) for i in range(0,numPieces)]
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
        
        # special case if roll == 6 and no pieces in play
        if roll == 6 and not(self.__activePieces):
            self.leaveHome()
        elif not(self.__activePieces): # if no pieces in play 
            return
        else: # if active pieces
            self.moveHeuristic(roll)

    def leaveHome(self):
        """
        Moves a piece out of home base and onto board.
        """
        # move a piece out from home base and get its piece num
        self.__activePieces.append(self.__homePieces.pop())
        # move that piece to the start position
        self.__activePieces[-1]._Piece__boardPos = self.__startPos
        # update that piece's move count
        self.__activePieces[-1]._Piece__moveCount = 1
        
        # check if an opponent's piece was hit
        allPiecePosns = self.__board._Board__piecePosns
        othersPosns = [allPiecePosns[key] for key in allPiecePosns.keys()
                      if key[0] != str(self.__id)]
        if self.__activePieces[-1]._Piece__boardPos in othersPosns:
            canHitPos = self.__startPos
        else:
            canHitPos = []
        
        if canHitPos:
            self.hitPiece(self.__startPos)
        
        # update board `__piecePosns`
        pieceID = self.__activePieces[-1]._Piece__pieceID
        self.__board._Board__piecePosns[str(self.__id)+str(pieceID)] = (
            self.__startPos)
    
    def moveHeuristic(self, roll):
        """
        Uses heuristics to pick which piece to move, based on (in order of
        preference): 1) trying to hit another player's piece, 2) not moving 
        within a die roll of another player's piece, 3) moving up in the score 
        arm. This function also makes sure a potential move cannot take place
        if that move would overtake a block.
        
        Parameters
        ----------
        roll: a simulated die roll
        
        Examples
        --------
        roll = np.random.randint(1,7)
        p.moveHeuristic(roll)
        
        p.moveHeuristic(6)   
        """        
        # get necessary info from board
        allPiecePosns = self.__board._Board__piecePosns
        boardSpaces = self.__board._Board__boardSpaces
        scoreArmSpaces = self.__board._Board__scoreArmSpaces
        
        # get positions of all other pieces
        othersPosns = [allPiecePosns[key] for key in allPiecePosns.keys()
                      if key[0] != str(self.__id)]
        
        # out of all possible pieces to move, get `pieceToMove` (`__pieceID`
        # for the piece we want to move):
        
        pieceToMove = []
        
# cmntd out: using `map` and `zip(*)` to unzip two lists       
        # get our potential positions
#        activePieceIDs, rollPosns = (
#            map(list, zip(
#                *[[self.__activePieces[piece]._Piece__pieceID, 
#                self.__activePieces[piece]._Piece__boardPos + roll] 
#                for piece in range(0, len(self.__activePieces))])))
        
        # get our active piece IDs
        activePieceIDs = [self.__activePieces[piece]._Piece__pieceID 
                          for piece in range(0, len(self.__activePieces))]
        # get our potential positions
        rollPosns = [self.__activePieces[piece]._Piece__boardPos + roll
                    for piece in range(0, len(self.__activePieces))]
        # get our potential move counts
        rollMoveCounts = [self.__activePieces[piece]._Piece__moveCount + roll 
                         for piece in range(0, len(self.__activePieces))]
        # get our potential score arm positions
        rollScoreArmPosns = [self.__activePieces[piece]._Piece__scoreArmPos + roll
                            for piece in range(0, len(self.__activePieces))]
        
        # check to see if there are any blocks:
        blockPosns = [pos for pos, count 
                     in collections.Counter(othersPosns).items() 
                     if count > 1 and pos > 0]
        
        # check to see if we can hit another piece
        canHitPos = [pos for pos in rollPosns 
                     if (pos in othersPosns and not(pos in blockPosns))]
        
        # check to see if we can move in score arm
        canMoveInScoreArm = [
            activePieceIDs[piece] for piece in range(0, len(activePieceIDs)) 
            if rollMoveCounts[piece] >= boardSpaces # if we are in score arm
            and rollScoreArmPosns[piece] <= (scoreArmSpaces+1)] # and our move wouldn't be past score arm
                    
        # if, elif, elif, else block for 1) hitting another piece, 2) moving up
        # in score arm, 3) not moving past a block, 4) random move
        if canHitPos:
            pieceToMove = activePieceIDs[rollPosns.index(canHitPos[0])]
        elif canMoveInScoreArm: # if we have a piece in score arm, move it, else check for blocks
            pieceToMove = canMoveInScoreArm[0]
        elif blockPosns:    
            piecesToMove = [activePieceIDs[piece] for piece 
                           in range(0, len(self.__activePieces)) 
                           for block in range(0, len(blockPosns))
                           if (rollPosns[piece] < blockPosns[block])]
            
            if piecesToMove:                  
                pieceToMove = random.choice(piecesToMove)
                
        else:
            # prune available pieces to those not stuck in score arm           
            piecesToMove = [
                self._Player__activePieces[piece]._Piece__pieceID 
                for piece in range(0, len(activePieceIDs))
                if self._Player__activePieces[piece]._Piece__scoreArmPos <= 0]
            
            if piecesToMove:
                if roll == 6:
                    toLeaveHome = random.randint(0,1)
                    if toLeaveHome:
                        self.leaveHome()
                        return
                    
                else:
                    pieceToMove = random.choice(piecesToMove)

        # if no possible moves
        if pieceToMove == []:
            if roll == 6 and self.__homePieces:
                self.leaveHome()
                return
            else:
                return
        
        self.updateGame(roll, pieceToMove, activePieceIDs, canHitPos)
            
    def updateGame(self, roll, pieceToMove, activePieceIDs, canHitPos):
        """
        Updates the game state after a player rolls and decides which piece to
        move.
        
        Parameters
        ----------
        roll: a number representing a simulated die roll
        pieceToMove: a number of the piece ID to be moved
        activePieceIDs: a numeric array of the piece IDs of the player's 
            active pieces
        canHitPos: a number representing the board position on which a hit move 
            will take place (this value will be empty if a hit move is not 
            possible)
        
        Examples
        --------
        
        """
        # the move: 1) update piece `__boardPos`, `__moveCount`, `__scoreArmPos`;
        # 2) update player '__score' and '__scorePieces'; 
        # 3) update board `__score` and `__piecePosns`     

        activePieceIndx = activePieceIDs.index(pieceToMove)
        boardPos = self.__activePieces[activePieceIndx]._Piece__boardPos
        moveCount = self.__activePieces[activePieceIndx]._Piece__moveCount
        scoreArmSpaces = self.__board._Board__scoreArmSpaces
        boardSpaces = self.__board._Board__boardSpaces

        # update piece `__boardPos` and `__moveCount`
        boardPos += roll
        self.__activePieces[activePieceIndx]._Piece__boardPos = boardPos        
        moveCount += roll
        self.__activePieces[activePieceIndx]._Piece__moveCount = moveCount
        
        # if one player can hit another's piece
        if canHitPos:
            # move hit piece back to home pos
            self.hitPiece(boardPos)
        else:            
            # if we are in the score arm...
            if moveCount > boardSpaces:
                # update `__scoreArmPos`
                scoreArmPos = moveCount - boardSpaces
                self.__activePieces[activePieceIndx]._Piece__scoreArmPos = scoreArmPos
                # remove piece from board
                self.__activePieces[activePieceIndx]._Piece__boardPos = -1000
                self.__board._Board__piecePosns[str(self.__id)+str(pieceToMove)] = - 1000
                
                # see if piece scored
                if moveCount > (boardSpaces + scoreArmSpaces):
                    # update score
                    self.__score += 1
                    self.__board._Board__scores[self.__id] = self.__score
                    # add piece to `__scorePieces` and remove from `__activePieces`
                    self.__scorePieces.append(self.__activePieces.pop(activePieceIndx))
                    return # so we don't update board `__piecePosns` as below
        
        # update board `__piecePosns`
        self.__board._Board__piecePosns[str(self.__id)+str(pieceToMove)] = (
            self.__activePieces[activePieceIndx]._Piece__boardPos)
        
    
    def hitPiece(self, boardPos):
        """
        Executes the mechanics of finding out which opponent's piece was hit
        when a hit move is executed, and updates the board accordingly.
        
        Parameters
        -----------
        boardPos: the new boardPos of the piece that will be moved
        
        Examples
        --------
        
        """
        # get opponent's piece which is hit:
        allPiecePosns = self.__board._Board__piecePosns
        # get string val of hit playerID and pieceID 
        oppoPlayerID, oppoPieceID = (
            list(allPiecePosns.keys())[list(allPiecePosns.values()).index(boardPos)])
        # get hit Player object
        oppoPlayer = (
            [self.__board._Board__players[player] for player 
             in range(0, self.__board._Board__numPlayers) 
             if self.__board._Board__players[player]._Player__id 
             == int(oppoPlayerID)])[0]
        # get hit Piece object and index of piece in opponent's
        # `__activePieces` together as tuple
        oppoActivePieceNIndx = (
            [(oppoPlayer._Player__activePieces[piece], piece) for piece 
            in range(0, len(oppoPlayer._Player__activePieces)) 
            if oppoPlayer._Player__activePieces[piece]._Piece__pieceID
            == int(oppoPieceID)])
        
        # update that piece's and board's piece pos
        oppoActivePieceNIndx[0][0]._Piece__boardPos = -1000
        oppoActivePieceNIndx[0][0]._Piece__moveCount = -1000
        oppoActivePieceNIndx[0][0]._Piece__scoreArmPos = -1000
        self.__board._Board__piecePosns[oppoPlayerID+oppoPieceID] = -1000
        # move hit piece back to opponent's home base
        oppoPlayer._Player__homePieces.append(oppoPlayer._Player__activePieces.pop(oppoActivePieceNIndx[0][1]))
        
