import sys
sys.path.append('/Users/kovu/Documents/Projects/Blockchain/Blockchain_learn/')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from ..util import hash256
import time

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()
        
    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)
        
    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Codies Alert sent {BlockHeight} Bitcoins to Kovu"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockHeader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockHeader.mine()
        self.chain.append(Block(BlockHeight, 1, blockHeader, 1, Transaction))
        print(self.chain)
        
if __name__ =="__main___":
    blockchain = Blockchain()