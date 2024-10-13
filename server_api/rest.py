import flask
from flask import Flask, render_template, request
import blockchain.whitelist as whitelist
import json
import blockchain.transaction as transaction

app = Flask(__name__)


def parse_arg(parsed_arg):
    get_arg = request.args.get(parsed_arg)
    return get_arg.replace(" ", "")


def check_api_key(api_key):
    if api_key != "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa":
        return flask.abort(403)


@app.route("/check_balance", methods=["GET"])
def check_balance():
    check_api_key(parse_arg("k"))

    address = parse_arg("address")
    balance = transaction.get_balance(address)
    return json.dumps({"balance": balance})


@app.route("/award_tokens", methods=["GET"])
def award_tokens():
    check_api_key(parse_arg("k"))

    address = parse_arg("address")
    amount = int(parse_arg("amount"))

    transaction.award_tokens(address, amount)
    balance = transaction.get_balance(address)
    return json.dumps({"succeeded": True, "curr_balance": balance})


@app.route("/transfer_tokens", methods=["GET"])
def transfer_tokens():
    check_api_key(parse_arg("k"))

    sending_address = parse_arg("send_address")
    receiving_address = parse_arg("recv_address")
    sending_priv_key = parse_arg("send_priv_key")
    amount = int(parse_arg("amount"))

    transaction.transfer_tokens(sending_priv_key, sending_address, receiving_address, amount)
    balance = transaction.get_balance(sending_address)
    return json.dumps({"succeeded": True, "curr_balance": balance})


@app.route("/add_whitelist", methods=["GET"])
def add_to_whitelist():
    check_api_key(parse_arg("k"))

    address = parse_arg("address")

    whitelist.add_to_whitelist(address)
    return json.dumps({"succeeded": True})


@app.route("/remove_whitelist", methods=["GET"])
def remove_from_whitelist():
    check_api_key(parse_arg("k"))

    address = parse_arg("address")

    whitelist.remove_from_whitelist(address)
    return json.dumps({"succeeded": True})

if __name__ == "__main__":
    app.run(debug=True)
