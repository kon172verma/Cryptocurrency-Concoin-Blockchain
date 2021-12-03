from concoin import Concoin
import random, string

concoin = Concoin()
for i in range(13):
    sender = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    receiver = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    amount = random.randint(1,1000)
    concoin.add_transaction(sender, receiver, amount)
print(concoin.transactions_pool)

print(len(concoin.transactions_pool))
concoin.mine_block()

print(len(concoin.transactions_pool))
concoin.mine_block()

print(len(concoin.transactions_pool))
concoin.mine_block()

print(len(concoin.transactions_pool))
concoin.mine_block()

print(len(concoin.transactions_pool))
for i in concoin.chain:
    print(i)