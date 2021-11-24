# Importing the required modules and libraries.
from blockchain import Blockchain
from flask import Flask
from flask.globals import request
import json

# Creating our Flask web app.
app = Flask(__name__)

# Initializing our blockchain.
blockchain = Blockchain()

# Route - home: Displays the entire blockchain.
@app.route('/', methods=['GET'])
def home():
    response = json.dumps(blockchain.getChain())
    return response, 200

# Route - addBlock: Adds a new block to our blockchain. 
@app.route('/mineBlock', methods=['GET'])
def mineBlock():
    data = request.args.get('data')
    # print(data)
    if data == None:
        return 'Block not mined. Empty data.!'
    blockchain.addBlock(data)
    return 'New block mined and is added to the blockchain', 200

# Route - verify: Verifies the entire blockchain.
@app.route('/verifyChain', methods=['GET'])
def verifyChain():
    response = ''
    if blockchain.verifyChain():
        response = 'Blockchain verified.!'
    else:
        response = 'Blockchain data not correct.!'
    return response, 200

# Running our web app.
app.run('localhost', 8080)