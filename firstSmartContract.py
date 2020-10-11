#4
from web3 import Web3
import json

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]


abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = "0xFc495f1C11Ef1eE31CE285dc7aB2b87c9b0A8cF2"

contract = web3.eth.contract(address = address,abi = abi)

print(f"Previous Contract Greeting : {contract.functions.greet().call())}")

#creates a transaction on blockchain to make a change
tx_hash = contract.functions.setGreeting("Promepy Thope").transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print(f"Updated Contract Greeting : {contract.functions.greet().call())}")