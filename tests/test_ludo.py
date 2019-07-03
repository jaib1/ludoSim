# import pdb
# pdb.set_trace()
# import pytest
from ludoSim import *

#class TestLudo(object):
#    """
#    A test class for the `ludoSim` module 
#    
#    Examples
#    ---------
#    import pytest
#    pytest.main(['test_ludo.py'])
#    """
#    
#    def test_roll(self):
#        """ 
#        Tests outcomes of a die roll given certain game states
#        """
#        
#        self.player = Player(1,4,1,52, [-1000, -1000, -1000, -1000])
#        # first test: move piece out of home base
#        roll = 6
#        
#        # should be empty initially
#        assert not(self.player.__activePieces) 
#        
#        # should be -1000 (indicates off board)
#        assert self.player.__pieces._Piece.__boardPos[-1] == -1000
#        
#        self.player.makeMove(roll) # move piece out of home base 
#        
#        # number of first active piece should be number of last piece
#        assert self.player.__activePieces[0]._Piece__pieceNum == self.player.__pieces[0]._Piece__pieceNum
#        
#        # check for update of board position and move count
#        assert self.player.__activePieces[0]._Piece__boardPos == self.player.__startPos
#        assert self.player.__activePieces[0]._Piece__moveCount == 1

def test_roll():
    """ 
    Tests outcomes of a die roll given certain game states
    """
    b = Board()
    p = b._Board__players[0]
    # first test: move piece out of home base
    roll = 6
    
    # should be empty initially
    assert not(p._Player__activePieces) 

    # should be -1000 (indicates off board)
    assert p._Player__pieces[-1]._Piece__boardPos == -1000
    
    p.makeMove(roll) # move piece out of home base 
    
    # number of first active piece should be number of last piece
    assert p._Player__activePieces[0]._Piece__pieceNum == p._Player__pieces[-1]._Piece__pieceNum
    
    # check for update of board position and move count
    assert p._Player__activePieces[0]._Piece__boardPos == p._Player__startPos
    assert p._Player__activePieces[0]._Piece__moveCount == 1

def test_score():
    """
    Tests whether a score occurs when a player has a chance to move piece to 
    end of score arm
    """
    b = Board()
    p = b._Board__players[0]
    # get pieces onto board
    for piece in range(0, b._Board__numPieces):
        p._Player__activePieces.append(p._Player__homePieces.pop())
        # move that piece to the start position
        p._Player__activePieces[-1]._Piece__boardPos = p._Player__startPos
        # update that piece's move count
        p._Player__activePieces[-1]._Piece__moveCount = 1
    # `__homePieces` should now be empty
    assert not(p._Player__homePieces)
    # move one piece to score arm
    pz = p._Player__activePieces[-1]
    pz._Piece__boardPos = b._Board__boardSpaces
    pz._Piece__moveCount = b._Board__boardSpaces + 1
    p.makeMove(6) # score the piece

    import pdb
    pdb.set_trace()
    
