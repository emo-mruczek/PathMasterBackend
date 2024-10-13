from web3 import Web3
from config import get_var, send_transaction


def check_whitelist(address):
    return get_var("CONTRACT").functions.whitelist(address).call()


def add_to_whitelist(address_to_add):
    if not Web3.is_checksum_address(address_to_add):
        raise Exception("The added value is not a valid checksum address.")
    if check_whitelist(address_to_add):
        raise Exception("The address is already whitelisted.")
    nonce = get_var("WEB3").eth.get_transaction_count(get_var("OWNER_ADDRESS"))
    txn = get_var("CONTRACT").functions.addToWhitelist(address_to_add).build_transaction({
        'chainId': get_var("CHAIN_ID"),  # Ganache local testnet default chain ID
        'gas': 2000000,
        'gasPrice': get_var("WEB3").to_wei(get_var("GAS_PRICE"), 'gwei'),
        'nonce': nonce
    })
    txn_hash = send_transaction(txn, get_var("OWNER_PRIVATE_KEY"))
    print(f"Added {address_to_add} to whitelist. Hash: {txn_hash}.")


def remove_from_whitelist(address_to_remove):
    if not check_whitelist(address_to_remove):
        print(f"{address_to_remove} is not on whitelist.")
        raise Exception(f"{address_to_remove} is not on whitelist.")
    nonce = get_var("WEB3").eth.get_transaction_count(get_var("OWNER_ADDRESS"))
    txn = get_var("CONTRACT").functions.removeFromWhitelist(address_to_remove).build_transaction({
        'chainId': get_var("CHAIN_ID"),
        'gas': 2000000,
        'gasPrice': get_var("WEB3").to_wei(get_var("GAS_PRICE"), 'gwei'),
        'nonce': nonce
    })
    txn_hash = send_transaction(txn, get_var("OWNER_PRIVATE_KEY"))
    print(f"Removed {address_to_remove} from whitelist. Hash: {txn_hash}.")
