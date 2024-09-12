class Block:
    """
    Storage container that stores transactions
    """
    def __init__(self, Height, Blocksize, BlockHeader, Txcount, Txs):
        self.Height = Height
        self.Blocksize = Blocksize
        self.Blockheader = BlockHeader
        self.Txcount = Txcount
        self.Txs = Txs
        pass