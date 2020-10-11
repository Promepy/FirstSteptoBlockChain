#6
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/359727a040944770a984e310f22b7932"
web3 = Web3(Web3.HTTPProvider(infura_url))


latest = web3.eth.blockNumber
print(latest)

print(web3.eth.getBlock(latest))

for i in range(0, 10):
    print(web3.eth.getBlock(latest - i))

hash = '0x00a38bc0c68e40fdf5d340c9e01fc81f8c16ee31d1f5d7f97f7740127a49648e'
print(web3.eth.getTransactionByBlock(hash, 2))