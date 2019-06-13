# import pdb
# pdb.set_trace()

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
    
    player = Player(1,4,1,52, [-1000, -1000, -1000, -1000])
    # first test: move piece out of home base
    roll = 6
    
    # should be empty initially
    assert not(player._Player__activePieces) 
    
    import pdb
    pdb.set_trace()
    # should be -1000 (indicates off board)
    assert player._Player__pieces[-1]._Piece__boardPos == -1000
    
    player.makeMove(roll) # move piece out of home base 
    
    # number of first active piece should be number of last piece
    assert player._Player__activePieces[0]._Piece__pieceNum == player._Player__pieces[-1]._Piece__pieceNum
    
    # check for update of board position and move count
    assert player._Player__activePieces[0]._Piece__boardPos == player._Player__startPos
    assert player._Player__activePieces[0]._Piece__moveCount == 1