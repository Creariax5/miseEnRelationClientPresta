from django.test import TestCase
from web3 import Web3


def give_btc(nb, address):
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    account_1 = '0x543322Cdc825779A98bE7d9da6799B789D96e94a'  # Fill me in
    account_2 = '0xdCf5305754e0A347635307A1ACc15A1F7BbA1dD6'  # Fill me in
    private_key = '1e9fb15dd5d52c56f3ce64811b51da9e4bffa18b5cd226d096c6c618b89e6370'  # Fill me in

    nonce = web3.eth.getTransactionCount(account_1)

    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': web3.toWei(nb/1000, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
    }

    signed_tx = web3.eth.account.signTransaction(tx, private_key)

    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    print(web3.toHex(tx_hash))

    print("give ", nb, " BTC")


