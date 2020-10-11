#1
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/359727a040944770a984e310f22b7932"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9")
print(web3.fromWei(balance, "ether"))