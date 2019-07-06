class Piece(): 
    """
    A class which represents a player's piece in a ludo game. Instantiated and used by `Board`.
    
    Attributes:
    -----------
        __playerID: the ID of the player the piece belongs to
        __pieceID: the number of the piece
        __moveCount: the current number of spaces the piece has moved
        __boardPos: the current board space the piece occupies
        __scoreArmPos: the current score arm space the piece occupies
    """
    
    # define and limit attributes:
    # we won't make them truly private (using `@property`), but will instead
    # make them hidden, using `__`
    __slots__ = ('__playerID', '__pieceID', '__boardPos', '__scoreArmPos', 
        '__moveCount')
        
    def __init__(self, playerID, pieceID):
        """
        The constructor requires the id of the player the piece belongs to.
        
        Parameters
        -----------
        playerID
        
        Examples
        --------
        p = Piece(1,1)
        
        p = Piece(pieceID=2, playerID=2)
        
        """
        
        self.__playerID = playerID
        self.__pieceID = pieceID
        self.__boardPos = -1000 # hacky placeholders for representing "off board"
        self.__moveCount = -1000 
        self.__scoreArmPos = -1000
        
    def __iter__(self):
        """
        Generator Function to use class as iterator.
        """