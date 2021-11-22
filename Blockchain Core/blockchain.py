import datetime

class Block:
    def __init__(self, index, data, nonce, prevHash) -> None:
        self.index = index
        self.timestamp = int(datetime.datetime.now().timestamp())
        self.data = data
        self.nonce = nonce
        self.prevHash = prevHash

class Blockchain:
    def __init__(self) -> None:
        self.chain = []

    def prevHash(self):
        if len(self.chain) == 0:
            return 0
        return self.chain[-1].prevHash

    def createBlock(self, data, nonce) -> None:
        block = Block(len(self.chain), data, nonce, self.prevHash())
        self.chain.append(block)

    def printchain(self) -> None:
        for i in self.chain:
            print(i.index, i.timestamp, i.data, i.proof, i.prevHash)

    

chain = Blockchain()
chain.createBlock('some string for now', 0)
chain.createBlock('some string for now', 1)
chain.createBlock('some string for now', 2)
chain.printchain()
