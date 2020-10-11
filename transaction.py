#3
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

account_1 = "0x01F91E836b974F05a82d9A87f3B6eA3B44F3633C"
account_2 = "0x12b220807a79832Ed14F3D6b28816085B910ce1c"

privateKey = "f90acefa74a6b1ce180e1707db1b27706e110a836e38dfdf6749d31cb878e37f"

#get the nonce
nonce = web3.eth.getTransactionCount(account_1)

#build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#sign transaction
signed_tx = web3.eth.account.signTransaction(tx, privateKey)

#send transaction and get transaction hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))