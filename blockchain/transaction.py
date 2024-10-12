from config import get_var, send_transaction
import whitelist


# Function to award tokens to a user
def award_tokens(user_address, token_amount):
    nonce = get_var("WEB3").eth.get_transaction_count(get_var("OWNER_ADDRESS"))
    txn = get_var("CONTRACT").functions.awardTokens(user_address, token_amount).build_transaction({
        'chainId': get_var("CHAIN_ID"),
        'gas': 2000000,
        'gasPrice': get_var("WEB3").to_wei('20', 'gwei'),
        'nonce': nonce
    })

    txn_hash = send_transaction(txn, get_var("OWNER_PRIVATE_KEY"))
    print(f"Awarded {token_amount} WTK to {user_address}. Hash: {txn_hash}.")


def get_balance(checked_address, silent=False):
    balance = get_var("CONTRACT").functions.balanceOf(checked_address).call()
    balance = float(balance / (10 ** get_var("DECIMALS")))
    if not silent:
        print(f"{checked_address} has {balance} WTK.")
    return balance

# Function to transfer tokens between whitelisted addresses
def transfer_tokens(sender_private_key, sender_address, recipient_address, token_amount):
    if not whitelist.check_whitelist(recipient_address):
        raise Exception("Receiving address is not on whitelist.")
    if float(get_balance(sender_address, True)) / (10 ** get_var("DECIMALS")) < token_amount:
        raise Exception("Sender does not have enough tokens.")
    nonce = get_var("WEB3").eth.get_transaction_count(sender_address)
    txn = get_var("CONTRACT").functions.transfer(recipient_address, token_amount).build_transaction({
        'chainId': get_var("CHAIN_ID"),
        'gas': 2000000,
        'gasPrice': get_var("WEB3").to_wei('20', 'gwei'),
        'nonce': nonce
    })
    # Sign and send the transaction
    txn_hash = send_transaction(txn, sender_private_key)
    print(f"Transferred {token_amount / (10 ** get_var("DECIMALS"))} WTK from {sender_address} to {recipient_address}. "
          f"Hash: {txn_hash}")
