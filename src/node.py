from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity)
from flask_restful import reqparse

from wallet import Wallet
from blockchain import TransactionBlockchain, FeedbackBlockchain, CitationBlockchain
from flask import Flask
from config.config import Config

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
CORS(app)


@app.route('/', methods=['GET'])
def get_node_ui():
    return render_template('index.html')


#@app.route('/network', methods=['GET'])
#def get_network_ui():
    #return send_from_directory('ui', 'network.html')


#@app.route('/user', methods=['GET'])
#def get_login_ui():
    #return send_from_directory('ui', 'login.html')


@app.route('/wallet', methods=['POST'])
def create_keys():
    wallet = Wallet(1) # Get rid of node later
    wallet.create_keys()
    if wallet.save_keys():
        global tx_chain
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': tx_chain.get_balance(wallet.public_key)
        }
        print(response)
        return jsonify(response), 201
    else:
        response = {
            'message': 'Saving the keys failed.'
        }
        return jsonify(response), 500


@app.route('/transaction/balance', methods=['GET'])
def get_balance():
    """Checks the public keys balance.

    Returns:
        Response: 
    """
    sender = None
    balance = blockchain.get_balance(sender=sender)
    if balance != None:
        response = {
            'message': 'Fetched balance successfully.',
            'funds': balance
        }
        return jsonify(response), 200
    else:
        response = {
            'messsage': 'Loading balance failed.',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500


@app.route('/cube/broadcast-transaction', methods=['POST'])
def broadcast_transaction():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400
    required = ['sender', 'recipient', 'signature', 'amount']
    if not all(key in values for key in required):
        response = {'message': 'Some data is missing.'}
        return jsonify(response), 400
    success = blockchain.add_transaction(
        values['sender'], values['recipient'], values['signature'], values['amount'], is_receiving=True)
    if success:
        response = {
            'message': 'Successfully added transaction.',
            'transaction': {
                'sender': values['sender'],
                'recipient': values['recipient'],
                'signature': values['signature'],
                'amount': values['amount']
            }
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed.'
        }
        return jsonify(response), 500


@app.route('/cube/broadcast-citation', methods=['POST'])
def broadcast_transaction():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400
    required = ['sender', 'platform', 'signature', 'payload']
    if not all(key in values for key in required):
        response = {'message': 'Some data is missing.'}
        return jsonify(response), 400
    success = blockchain.add_transaction(
        values['sender'], values['platform'], values['signature'], values['payload'], is_receiving=True)
    if success:
        response = {
            'message': 'Successfully added citation.',
            'transaction': {
                'sender': values['sender'],
                'platform': values['platform'],
                'signature': values['signature'],
                'payload': values['payload']
            }
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a citation failed.'
        }
        return jsonify(response), 500


@app.route('/cube/broadcast-feedback', methods=['POST'])
def broadcast_transaction():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400
    required = ['sender', 'platform', 'signature', 'payload']
    if not all(key in values for key in required):
        response = {'message': 'Some data is missing.'}
        return jsonify(response), 400
    success = blockchain.add_transaction(
        values['sender'], values['platform'], values['signature'], values['payload'], is_receiving=True)
    if success:
        response = {
            'message': 'Successfully added feedback.',
            'transaction': {
                'sender': values['sender'],
                'platform': values['platform'],
                'signature': values['signature'],
                'payload': values['payload']
            }
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating feedback failed.'
        }
        return jsonify(response), 500


@app.route('/block/broadcast-transaction', methods=['POST'])
def broadcast_block():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400
    if 'block' not in values:
        response = {'message': 'Some data is missing.'}
        return jsonify(response), 400
    block = values['block']
    if block['index'] == blockchain.chain[-1].index + 1:
        if blockchain.add_block(block):
            response = {'message': 'Block added'}
            return jsonify(response), 201
        else:
            response = {'message': 'Block seems invalid.'}
            return jsonify(response), 409
    elif block['index'] > blockchain.chain[-1].index:
        response = {'message': 'Blockchain seems to differ from local blockchain iteration.'}
        blockchain.resolve_conflicts = True
        return jsonify(response), 200
    else: 
        response = {'message': 'Blockchain seems to be shorter, block not added'}
        return jsonify(response), 409


@app.route('/transaction', methods=['POST'])
def add_transaction():
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data found.'
        }
        return jsonify(response), 400
    required_fields = ['public_key', 'private_key', 'recipient', 'payload']
    if not all(field in values for field in required_fields):
        response = {
            'message': 'Required data is missing.'
        }
        return jsonify(response), 400
    recipient = values['recipient']
    amount = values['amount']
    wallet = Wallet(values['public_key'], values['private_key'])
    signature = wallet.sign_transaction(wallet.public_key, recipient, amount)
    success = tx_chain.add_transaction(
        wallet.public_key, recipient, signature, amount)
    if success:
        response = {
            'message': 'Successfully added transaction.',
            'transaction': {
                'sender': wallet.public_key,
                'recipient': recipient,
                'amount': amount,
                'signature': signature
            },
            'funds': tx_chain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed.'
        }
        return jsonify(response), 500


@app.route('/citation', methods=['POST'])
def add_citation():
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data found.'
        }
        return jsonify(response), 400
    required_fields = ['public_key', 'private_key', 'recipient', 'payload']
    if not all(field in values for field in required_fields):
        response = {
            'message': 'Required data is missing.'
        }
        return jsonify(response), 400
    platform = values['platform']
    payload = values['payload']
    wallet = Wallet(values['public_key'], values['private_key'])
    signature = wallet.sign_transaction(wallet.public_key, platform, payload)
    success = ct_chain.add_transaction(
        wallet.public_key, platform, signature, payload)
    if success:
        response = {
            'message': 'Successfully added transaction.',
            'transaction': {
                'sender': wallet.public_key,
                'platform': platform,
                'payload': payload,
                'signature': signature
            },
            'funds': ct_chain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed.'
        }
        return jsonify(response), 500


@app.route('/feedback', methods=['POST'])
def add_feedback():
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data found.'
        }
        return jsonify(response), 400
    required_fields = ['public_key', 'private_key', 'recipient', 'payload']
    if not all(field in values for field in required_fields):
        response = {
            'message': 'Required data is missing.'
        }
        return jsonify(response), 400
    platform = values['platform']
    payload = values['payload']
    wallet = Wallet(values['public_key'], values['private_key'])
    signature = wallet.sign_transaction(wallet.public_key, platform, payload)
    success = fb_chain.add_transaction(
        wallet.public_key, platform, signature, payload)
    if success:
        response = {
            'message': 'Successfully added transaction.',
            'transaction': {
                'sender': wallet.public_key,
                'platform': platform,
                'payload': payload,
                'signature': signature
            },
            'funds': fb_chain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed.'
        }
        return jsonify(response), 500


@app.route('/fake', methods=['POST'])
def mine():
    if True:
        response = {'error': 'This endpoint is not available as Crystal does not supprt the mining of Blocks'}
        return jsonify(response), 500
    if blockchain.resolve_conflicts == True:
        response = {'message': 'Resolve conflicts first. Block not added.'}
        return jsonify(response), 409
    block = blockchain.new_block()
    if block != None:
        dict_block = block.__dict__.copy()
        dict_block['transactions'] = [
            tx.__dict__ for tx in dict_block['transactions']]
        response = {
            'message': 'Block added successfully.',
            'block': dict_block,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Adding a block failed.',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500


@app.route('/resolve-conflicts', methods=['POST'])
def resolve_conflicts():
    replaced = blockchain.resolve()
    if replaced:
        response = {'message': 'Chain was replaced.'}
    else:
        response = {'message': 'Local chain kept.'}
    return jsonify(response), 200


@app.route('/transactions', methods=['GET'])
def get_open_transaction():
    transactions = blockchain.get_open_transactions()
    dict_transactions = [tx.__dict__ for tx in transactions]
    return jsonify(dict_transactions), 200


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_snapshot = blockchain.chain
    dict_chain = [block.__dict__.copy() for block in chain_snapshot]
    for dict_block in dict_chain:
        dict_block['transactions'] = [
            tx.__dict__ for tx in dict_block['transactions']]
    return jsonify(dict_chain), 200


@app.route('/node', methods=['POST'])
def add_node():
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data attached.'
        }
        return jsonify(response), 400
    if 'node' not in values:
        response = {
            'message': 'No node data found.'
        }
        return jsonify(response), 400
    node = values['node']
    blockchain.add_peer_node(node)
    response = {
        'message': 'Node added successfully.',
        'all_nodes': blockchain.get_peer_nodes()
    }
    return jsonify(response), 201


@app.route('/node/<node_url>', methods=['DELETE'])
def remove_node(node_url):
    if node_url == '' or node_url == None:
        response = {
            'message': 'No node found.'
        }
        return jsonify(response), 400
    blockchain.remove_peer_node(node_url)
    response = {
        'message': 'Node removed',
        'all_nodes': blockchain.get_peer_nodes()
    }
    return jsonify(response), 200


@app.route('/nodes', methods=['GET'])
def get_nodes():
    nodes = blockchain.get_peer_nodes()
    response = {
        'all_nodes': nodes
    }
    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    tx_chain = TransactionBlockchain()
    fb_chain = FeedbackBlockchain()
    ct_chain = CitationBlockchain()
    app.run(host='0.0.0.0', port=port, debug=True)