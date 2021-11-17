import datetime


class Blockchain:
    def __init__(self):
        # Initializing an empty blockchain
        self.chain = []
        # Created the genesis block
        self.createBlock(1, 0)

    def createBlock(self, proof, prevHash):
        # Declaring the structure of our block
        block = {
            'index': len(self.chain),
            'timestamp': datetime.datetime.now(),
            'data': [],
            'proof': proof,
            'prevHash': prevHash
        }
        # Appending the newly created block to our chain
        self.chain.append(block)


blockchain = Blockchain()
blockchain.createBlock(2, 1)
print(blockchain.chain)
