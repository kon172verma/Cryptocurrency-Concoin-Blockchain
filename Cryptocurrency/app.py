# Importing the required libraries and modules.
from concoin import Concoin
from flask import Flask
from flask.templating import render_template
import json
import random
import string

# Initializing our app.
app = Flask(__name__)

# Initializing the blockchain for cryptocurrency-concoin.
concoin = Concoin()

# Route to print all the blocks in our blockchain.
@app.route('/', methods=['GET'])
def home():
    response = json.dumps(concoin.chain, indent = 4, separators = (',', ': '))
    return render_template( 'results.html', response = response ), 200

# Route to mine a new block.
@app.route('/mine_block', methods=['GET'])
def mine_block():
    result = concoin.mine_block()
    response = 'New block mined successfully' if result else 'Not enough transactions.'
    return response, 200

# Route to add a bunch of random transactions.
@app.route('/add_random_transactions', methods=['GET'])
def add_random_transactions():
    for i in range(13):
        sender = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        receiver = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        amount = random.randint(1,1000)
        concoin.add_transaction(sender, receiver, amount)
    response = json.dumps(concoin.transactions_pool, indent = 4, separators = (',', ': '))
    return render_template( 'results.html', response = response ), 200

# Route to verify the entire blockchain.
@app.route('/verify_chain', methods=['GET'])
def verify_chain():
    result = concoin.verify_chain()
    response = 'Chain verified. Everything is okay.' if result else 'Chain corrupted.'
    return response, 200

# Running our flask app.
app.run('localhost', 5000)