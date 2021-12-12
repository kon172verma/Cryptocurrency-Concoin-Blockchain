# Importing the required libraries and modules.
from blockchain import Blockchain
from urllib.parse import urlparse
import time

# Creating the class for our cryptocurrency: Concoin.
class Concoin(Blockchain):
    # Initializing our blockchain and mempool for transactions.
    def __init__(self) -> None:
        super().__init__()
        self.transactions_pool = []
        self.nodes = set()

    # Function to add a new node to our nodes set.
    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    # Function to add transaction to our mempool.
    def add_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.transactions_pool.append(transaction)

    # Function to get the list of maximum first five transactions.
    def get_transaction_data(self):
        if len(self.transactions_pool) < 5:
            return self.transactions_pool.copy()
        return self.transactions_pool[:5].copy()

    # Function to remove the same number of transactions as we added to a new block.
    def remove_transactions(self, n):
        if len(self.transactions_pool) == n:
            self.transactions_pool = []
        self.transactions_pool = self.transactions_pool[n:]

    # Function to mine a new block.
    def mine_block(self):
        data = self.get_transaction_data()
        if data == []:
            print('Empty transaction pool.!')
            return False
        time.sleep(1)
        self.add_block(data)
        self.remove_transactions(len(data))
        return True
