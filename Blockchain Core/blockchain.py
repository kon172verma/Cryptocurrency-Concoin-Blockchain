# Importing the required libraries.
import datetime
import hashlib
import json


# Defined class for a block.
class Block:
    # A block has the following values: index(block number), timestamp(time of block creation), 
    # nonce(number to be used once for PoW), data(information that needs to be stored on the blockchain),
    # prevHash(hash of the previous block), hash(hash value of the current block).
    def __init__(self, index, data, prevHash) -> None:
        self.index = index
        self.timestamp = int(datetime.datetime.now().timestamp())
        self.nonce = 'YTD'
        self.data = data
        self.prevHash = prevHash
        self.hash = 'YTD'


# Defined class for blockchain and its required operations.
class Blockchain:
    # Initialized an empty list for blockchain.
    def __init__(self) -> None:
        self.chain = []

    # Function to print all the blocks in our blockchain.
    def printchain(self) -> None:
        for i in self.chain:
            print(i.index, i.timestamp, i.data, i.nonce, i.prevHash, i.hash)

    # Function to fetch the hash of the last block in our blockchain.
    def prevHash(self):
        if len(self.chain) == 0:
            return 0
        return self.chain[-1].hash

    # Function to create a new object of the class block.
    def createBlock(self, data):
        return Block(len(self.chain), data, self.prevHash())

    # Function to compute the Proof of Work(PoW): nonce and the hash value.
    # Here we have used SHA-256, and the target is the hash value with '0000' as prefix.
    def pow(self, block) -> None:
        jsonData = {
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'nonce': block.nonce,
            'prevHash': block.prevHash
        }
        nonce = 0
        while True:
            jsonData['nonce'] = nonce
            value = hashlib.sha256((json.dumps(jsonData, sort_keys=True)).encode()).hexdigest()
            if value[:4] == '0000':
                break
            nonce += 1
        return nonce, value

    # Function to add a new block to our blockchain.
    def addBlock(self):
        data = 'some data for now'
        block = self.createBlock(data)
        block.nonce, block.hash = self.pow(block)
        self.chain.append(block)

    # Function to verify our blockchain.
    def verifyChain(self) -> bool:

        # Test for verifing the Genesis block.
        if len(self.chain) == 1 and (
                self.chain[0].index != 0 
                or self.chain[0].prevHash != 0
                or hashlib.sha256((json.dumps({
                    'index': self.chain[0].index,
                    'timestamp': self.chain[0].timestamp,
                    'data': self.chain[0].data,
                    'nonce': self.chain[0].nonce,
                    'prevHash': self.chain[0].prevHash
                }, sort_keys=True)).encode()).hexdigest() != self.chain[0].hash 
            ):
            return False
        
        # Test for verifing the rest of the chain.
        if len(self.chain)>1:
            for i in range(1,len(self.chain)):
                if self.chain[i].index != i \
                    or self.chain[i].prevHash != self.chain[i-1].hash \
                    or hashlib.sha256((json.dumps({
                        'index': self.chain[i].index,
                        'timestamp': self.chain[i].timestamp,
                        'data': self.chain[i].data,
                        'nonce': self.chain[i].nonce,
                        'prevHash': self.chain[i].prevHash
                    }, sort_keys=True)).encode()).hexdigest() != self.chain[i].hash:
                    # or self.chain[i].timestamp - self.chain[i-1].timestamp <= 0:
                    return False
        return True