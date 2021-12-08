# Importing the required libraries and modules.
from flask.templating import render_template
from flask import Flask, redirect, request
from concoin import Concoin
import string, random

# Initializing our app.
app = Flask(__name__)

# Initializing the blockchain for cryptocurrency-concoin.
concoin = Concoin()

# Declaraing a global variable for sending alert message.
alert = ''

# Route to the index page, to display blockchain, transaction and .
@app.route('/', methods=['GET'])
def home():
    return render_template(
        'index.html',
        blockchain=concoin.chain,
        transactions=concoin.transactions_pool,
        alert=alert
    ), 200

# Route to mine a block, and redirect to home.
@app.route('/mine_block', methods=['GET'])
def mine_block():
    result = concoin.mine_block()
    global alert
    alert = 'New block #'+ str(len(concoin.chain)) +' mined successfully.' if result else 'Transactions pool empty. Can not mine a new block.'
    return redirect('/'), 302

# Route to verify the blockchain, and redirect to home.
@app.route('/verify_chain', methods=['GET'])
def verify_chain():
    result = concoin.verify_chain()
    global alert
    alert = 'Chain verified. Everything is okay.' if result else 'Chain corrupted.'
    return redirect('/'), 302

# Route to add transaction to transaction pool, and redirect to home.
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    try:
        sender = request.form.get('sender')
        receiver = request.form.get('receiver')
        amount = request.form.get('amount')
        concoin.add_transaction(sender, receiver, amount)
    except:
        print('Unable to add a requested transaction to the pool.')
    return redirect('/'), 302

# Route to add random transactions, and redirect to home.
@app.route('/add_random_transactions', methods=['GET'])
def add_random_transactions():
    try:
        count = int(request.args.get('transaction-number'))
    except:
        count = 7
    for i in range(count):
        sender = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        receiver = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        amount = random.randint(1,1000)
        concoin.add_transaction(sender, receiver, amount)
    return redirect('/'), 302

# Running our flask app.
app.run('localhost', 5000, debug=True)
