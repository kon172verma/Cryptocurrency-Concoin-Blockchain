import datetime
import hashlib
import json
class Block:
    def __init__(self, index, data, prevHash) -> None:
        self.index = index
        self.timestamp = int(datetime.datetime.now().timestamp())
        self.nonce = 'YTD'
        self.data = data
        self.prevHash = prevHash
        self.hash = 'YTD'

class Blockchain:
    def __init__(self) -> None:
        self.chain = []

    def printchain(self) -> None:
        for i in self.chain:
            print(i.index, i.timestamp, i.data, i.nonce, i.prevHash, i.hash)

    def prevHash(self):
        if len(self.chain) == 0:
            return 0
        return self.chain[-1].hash

    def createBlock(self, data):
        return Block(len(self.chain), data, self.prevHash())

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

    def addBlock(self):
        data = 'some data for now'
        block = self.createBlock(data)
        block.nonce, block.hash = self.pow(block)
        self.chain.append(block)

chain = Blockchain()
chain.addBlock()
chain.addBlock()
chain.addBlock()
chain.printchain()
