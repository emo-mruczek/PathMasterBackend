from web3 import Web3
import json


def send_transaction(txn, private_key):
    signed_txn = get_var("WEB3").eth.account.sign_transaction(txn, private_key=private_key)
    txn_hash = get_var("WEB3").eth.send_raw_transaction(signed_txn.raw_transaction)
    return get_var("WEB3").to_hex(txn_hash)


# Connect to Ethereum network (e.g., Infura Rinkeby testnet)
network_url = "http://127.0.0.1:8545/"
WEB3 = Web3(Web3.HTTPProvider(network_url))

# Check if the connection is successful
if not WEB3.is_connected():
    print(f"Connection failed.")
    exit(-1)

# Load contract ABI from a JSON file or string
abi_token_path = "/home/user/Source_Codes/contract_js/artifacts/contracts/WhitelistedToken.sol/WhitelistedToken.json"
with open(abi_token_path) as f:
    contract_abi = json.load(f)["abi"]

# Create a contract object
contract_address = Web3.to_checksum_address("0x5fbdb2315678afecb367f032d93f642f64180aa3".lower())
CONTRACT = WEB3.eth.contract(address=contract_address, abi=contract_abi)


config = {
    "OWNER_ADDRESS": CONTRACT.functions.owner().call(),
    "CHAIN_ID": 31337,
    "OWNER_PRIVATE_KEY": "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80",
    "CONTRACT": CONTRACT,
    "WEB3": WEB3,
    "DECIMALS": 0,
    "GAS_PRICE": 15,
}


def get_var(name):
    return config[name]