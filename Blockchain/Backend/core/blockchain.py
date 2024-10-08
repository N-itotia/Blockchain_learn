import sys
sys.path.append('D:\\Projects\\Blockchain_learn')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256
import time
import json

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
        self.chain.append(Block(BlockHeight, 1, blockHeader.__dict__, 1, Transaction).__dict__)
        print(json.dumps(self.chain, indent = 4))
    
    def main(self):
        while True:
            lastBlock = self.chain[::-1]
            BlockHeight = lastBlock[0]["Height"] + 1
            prevBlockHash = lastBlock[0]['BlockHeader']['blockHash']
            self.addBlock(BlockHeight, prevBlockHash)
        
<<<<<<< HEAD
if __name__ == "__main__":
    blockchain = Blockchain()
=======
if __name__ =="__main__":
    blockchain = Blockchain()
    blockchain.main()
>>>>>>> bd3e0c1ff27b19366fdce64f8ada2f718a3f432c
