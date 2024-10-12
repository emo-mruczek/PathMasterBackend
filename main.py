from blockchain.whitelist import *
from blockchain.transaction import *

first_key = Web3.to_checksum_address("0x70997970C51812dc3A010C7d01b50e0d17dc79C8".lower())
first_priv_key = "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d"
second_key = Web3.to_checksum_address("0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC".lower())
second_priv_key = "0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a"


# award_tokens(first_key, 10)
# add_to_whitelist(second_key)
transfer_tokens(second_priv_key, second_key, first_key, 30)

get_balance(first_key)
get_balance(second_key)