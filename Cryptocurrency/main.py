from flask.templating import render_template
from flask import Flask
from concoin import Concoin
import json
import string
import random


app = Flask(__name__)
concoin = Concoin()


@app.route('/', methods=['GET'])
def home():
    return render_template(
        'index.html',
        blockchain=concoin.chain,
        transactions=concoin.transactions_pool
    ), 200

@app.route('/mine_block', methods=['GET'])
def mine_block():
    result = concoin.mine_block()
    response = 'New block mined successfully' if result else 'Not enough transactions.'
    return response, 200

@app.route('/add_random_transactions', methods=['GET'])
def add_random_transactions():
    for i in range(13):
        sender = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        receiver = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        amount = random.randint(1,1000)
        concoin.add_transaction(sender, receiver, amount)
    response = json.dumps(concoin.transactions_pool, indent = 4, separators = (',', ': '))
    return render_template( 'results.html', response = response ), 200



app.run('localhost', 5000, debug=True)
