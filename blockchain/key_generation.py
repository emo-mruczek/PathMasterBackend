from web3 import Web3
import json


def gen_account():
    test = Web3().eth.account.create()
    priv_key = Web3.to_hex(test.key)
    address = test.address
    print(f"Private key: {priv_key}")
    print(f"Public key: {address}")
    return json.dumps({"private_key": priv_key, "address": address})

if __name__ == "__main__":
    gen_account()