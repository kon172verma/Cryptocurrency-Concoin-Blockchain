# Importing the required libraries.
import datetime
import json
import hashlib


# Defining the class for our blockchain.
class Blockchain:
    # Initializing the class with an empty chain.
    def __init__(self) -> None:
        self.chain = []

    # Function to fetch the hash of the last block in our chain.
    def get_prev_hash(self):
        if not len(self.chain):
            return 0
        return self.chain[-1]['hash']

    # Function to create a block with required initial values.
    def create_block(self, data):
        block = {
            'index': len(self.chain),
            'timestamp': int(datetime.datetime.now().timestamp()),
            'nonce': 'YTD',
            'data': data,
            'prev_hash': self.get_prev_hash(),
            'hash': 'YTD'
        }
        return block

    # Function for proof-of-work: uses SHA-256 to calculate the hash for our block.
    def proof_of_work(self, block):
        del block['hash']
        nonce = 0
        while True:
            block['timestamp'] = int(datetime.datetime.now().timestamp())
            block['nonce'] = nonce
            data = json.dumps(block, sort_keys=True).encode()
            hash_value = hashlib.sha256(data).hexdigest()
            if hash_value[:4] == '0000':
                return nonce, hash_value
            nonce += 1

    # Function to verify the proof-of-work for a given block.
    def verify_pow(self, block):
        hash_value = block['hash']
        del block['hash']
        if hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest() != hash_value:
            return False
        return True

    # Function that verifies our blockchain.
    def verify_chain(self):
        if len(self.chain) and not (
            self.chain[0]['index'] == 0 and
            self.chain[0]['prev_hash'] == 0
        ):
            return False
        for i in range(1, len(self.chain)):
            if self.chain[i]['index'] != i \
                    or self.chain[i]['timestamp'] < self.chain[i-1]['timestamp'] \
                    or self.chain[i]['prev_hash'] != self.chain[i-1]['hash'] \
                    or not self.verify_pow(self.chain[i].copy()):
                return False
        return True

    # Function to mine a new block with the given data.
    def mine_block(self, data='ABC'):
        block = self.create_block(data)
        block['nonce'], block['hash'] = self.proof_of_work(block)
        assert self.verify_chain(), 'Chain corrupted.!'
        self.chain.append(block)
