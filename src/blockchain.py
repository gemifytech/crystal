from functools import reduce
import hashlib as hl

import json
import pickle
import requests

# Import two functions from our hash_util.py file. Omit the ".py" in the import
from utility.hash_util import hash_block
from utility.verification import Verification
from block import Block
from transaction import Transaction, Feedback, Citation
from wallet import Wallet

# The reward we give to miners (for creating a new block)
FEEDBACK_REWARD = 1

class Blockchain:
    """The Blockchain class manages the chain of blocks, trans, and nodes.
    Attributes:
        :chain: The list of blocks
        :open_cubes (private): The list of open cubes
        :hosting_node: The connected node (which runs the blockchain).
    """

    def __init__(self, type):
        # Starting block
        genesis_block = Block(0, '', [], 100, 0)
        # Initializing our (empty) blockchain list
        self.chain = [genesis_block]
        # Unhandled cubes
        self.__open_cubes = []
        self.public_key = 0
        self.__peer_nodes = set()
        self.resolve_conflicts = False


    # This turns the chain attribute into a property with a getter (the method below) and a setter (@chain.setter)
    @property
    def chain(self):
        return self.__chain[:]

    # The setter for the chain property
    @chain.setter
    def chain(self, val):
        self.__chain = val

    def get_open_cubes(self):
        """Returns a copy of the open cubes list."""
        return self.__open_cubes[:]
    

    def proof_of_work(self):
        """Generate a proof of work for the open cubes, the hash of the previous block and a random number (which is guessed until it fits)."""
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        # Try different PoW numbers and return the first valid one
        while not Verification.valid_proof(self.__open_cubes, last_hash, proof):
            proof += 1
        return proof

    def get_last_blockchain_value(self):
        """ Returns the last value of the current blockchain. """
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]

    def add_peer_node(self, node):
        """Adds a new node to the peer node set.
        Arguments:
            :node: The node URL which should be added.
        """
        self.__peer_nodes.add(node)
        self.save_data()

    def remove_peer_node(self, node):
        """Removes a node from the peer node set.
        Arguments:
            :node: The node URL which should be removed.
        """
        self.__peer_nodes.discard(node)
        self.save_data()

    def get_peer_nodes(self):
        """Return a list of all connected peer nodes."""
        return list(self.__peer_nodes)

    def new_block(self):
        """Create a new block and add open cubes to it."""
        # Fetch the currently last block of the blockchain

        last_block = self.__chain[-1]
        
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        
        # Only benefit to copying is if we would like to reward platforms for initiating.
        copied_cubes = self.__open_cubes[:]
        for tx in copied_cubes:
            if not Wallet.verify_cubes(tx, self.type):
                return None
        block = Block(len(self.__chain), hashed_block,
                      copied_cubes, proof)
        
        self.__chain.append(block)
        self.__open_cubes = []
        self.save_data()
        
        for node in self.__peer_nodes:
            url = 'http://{}/block/broadcast'.format(node)
            converted_block = block.__dict__.copy()
            converted_block['cubes'] = [
                cube.__dict__ for cube in converted_block['cubes']]
            try:
                response = requests.post(url, json={'block': converted_block})
                if response.status_code == 400 or response.status_code == 500:
                    print('Block declined, needs resolving')
                if response.status_code == 409:
                    self.resolve_conflicts = True
            except requests.exceptions.ConnectionError:
                continue
        return block

class TransactionBlockchain(Blockchain):
    def __init__(self):
        super().__init__('tx')
        self.load_data()

    def load_data(self):
        """Initialize blockchain + open cubes data from a file."""
        try:
            with open('blockchain.txt', mode='r') as f:
                # file_content = pickle.loads(f.read())
                file_content = f.readlines()
                # blockchain = file_content['chain']
                # open_cubes = file_content['ot']
                blockchain = json.loads(file_content[0][:-1])
                # We need to convert  the loaded data because cubes should use OrderedDict
                updated_blockchain = []
                for block in blockchain:
                    converted_tx = [Transaction(
                        tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['cubes']]
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                open_cubes = json.loads(file_content[1][:-1])
                # We need to convert  the loaded data because cubes should use OrderedDict
                updated_cubes = []
                for tx in open_cubes:
                    updated_cube = Transaction(
                        tx['sender'], tx['recipient'], tx['signature'], tx['amount'])
                    updated_cubes.append(updated_cube)
                self._Blockchain__open_cubes = updated_cubes
                peer_nodes = json.loads(file_content[2])
                self._Blockchain__peer_nodes = set(peer_nodes)
        except (IOError, IndexError):
            pass
        finally:
            print('Cleanup!')

    def save_data(self):
        """Save blockchain + open cubes snapshot to a file."""
        try:
            with open('blockchain.txt', mode='w') as f:
                saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [
                    tx.__dict__ for tx in block_el.cubes], block_el.proof, block_el.timestamp) for block_el in self._Blockchain__chain]]
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_tx = [tx.__dict__ for tx in self._Blockchain__open_cubes]
                f.write(json.dumps(saveable_tx))
                f.write('\n')
                f.write(json.dumps(list(self._Blockchain__peer_nodes)))
                # save_data = {
                #     'chain': blockchain,
                #     'ot': open_cubes
                # }
                # f.write(pickle.dumps(save_data))
        except IOError:
            print('Saving failed!')

    def add_block(self, block):
        cubes = [Transaction(
            tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['cubes']]
        proof_is_valid = Verification.valid_proof(
            cubes[:-1], block['previous_hash'], block['proof'])
        hashes_match = hash_block(self.chain[-1]) == block['previous_hash']
        if not proof_is_valid or not hashes_match:
            return False
        converted_block = Block(
            block['index'], block['previous_hash'], cubes, block['proof'], block['timestamp'])
        self._Blockchain__chain.append(converted_block)
        stored_cubes = self._Blockchain__open_cubes[:]
        # The below is bad code
        for itx in block['cubes']:
            for opentx in stored_cubes:
                if opentx.sender == itx['sender'] and opentx.recipient == itx['recipient'] and opentx.amount == itx['amount'] and opentx.signature == itx['signature']:
                    try:
                        self._Blockchain__open_cubes.remove(opentx)
                    except ValueError:
                        print('Item was already removed')
        self.save_data()
        return True

    def resolve(self):
        winner_chain = self.chain
        replace = False
        for node in self._Blockchain__peer_nodes:
            url = 'http://{}/chain'.format(node)
            try:
                response = requests.get(url)
                node_chain = response.json()
                node_chain = [Block(block['index'], block['previous_hash'], [Transaction(
                    tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['cubes']],
                                    block['proof'], block['timestamp']) for block in node_chain]
                node_chain_length = len(node_chain)
                local_chain_length = len(winner_chain)
                if node_chain_length > local_chain_length and Verification.verify_chain(node_chain):
                    winner_chain = node_chain
                    replace = True
            except requests.exceptions.ConnectionError:
                continue
        self.resolve_conflicts = False
        self.chain = winner_chain
        if replace:
            self._Blockchain__open_cubes = []
        self.save_data()
        return replace

    def get_balance(self, sender=None):
        """Calculate and return the balance for a participant.
        """
        if sender == None:
            return "ERROR"
        else:
            participant = sender
        # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
        # This fetches sent amounts of cubes that were already included in blocks of the blockchain
        tx_sender = [[tx.amount for tx in block.cubes
                      if tx.sender == participant] for block in self._Blockchain__chain]
        # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
        # This fetches sent amounts of open cubes (to avoid double spending)
        open_tx_sender = [tx.amount
                          for tx in self._Blockchain__open_cubes if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                             if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
        # This fetches received coin amounts of cubes that were already included in blocks of the blockchain
        # We ignore open cubes here because you shouldn't be able to spend coins before the cube was confirmed + included in a block
        tx_recipient = [[tx.amount for tx in block.cubes
                         if tx.recipient == participant] for block in self._Blockchain__chain]
        amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                                 if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
        # Return the total balance
        return amount_received - amount_sent

    def add_cube(self, sender, recipient, signature, amount=1.0, is_receiving=False):
        """ Append a new value as well as the last blockchain value to the blockchain.
        Arguments:
            :sender: Tecihe sender of the coins.
            :rpient: The recipient of the coins.
            :amount: The amount of coins sent with the cube (default = 1.0)
        """
        cube = Transaction(sender, recipient, signature, amount)
        if Verification.verify_transaction(cube, self.get_balance):
            self._Blockchain__open_cubes.append(cube)
            self.save_data()
            if not is_receiving:
                for node in self.__peer_nodes:
                    url = 'http://{}/cube/broadcast-transaction'.format(node)
                    try:
                        response = requests.post(url, json={
                                                 'sender': sender, 'recipient': recipient,  'signature': signature, 'amount': amount})
                        if response.status_code == 400 or response.status_code == 500:
                            print('Transaction declined, needs resolving')
                            return False
                    except requests.exceptions.ConnectionError:
                        continue
            return True
        return False

class CitationBlockchain(Blockchain):
    def __init__(self):
        super().__init__('ct')

    def load_data(self):
        """Initialize blockchain + open cubes data from a file."""
        try:
            with open('fb_chain.txt', mode='r') as f:
                # file_content = pickle.loads(f.read())
                file_content = f.readlines()
                # blockchain = file_content['chain']
                # open_cubes = file_content['ot']
                blockchain = json.loads(file_content[0][:-1])
                # We need to convert  the loaded data because cubes should use OrderedDict
                updated_blockchain = []
                for block in blockchain:
                    converted_cube = [Citation(
                        cube['sender'], cube['platform'], cube['signature'], cube['payload']) for cube in block['cubes']]
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                open_cubes = json.loads(file_content[1][:-1])
                # We need to convert  the loaded data because cubes should use OrderedDict
                updated_cubes = []
                for cube in open_cubes:
                    updated_cube = Citation(
                        cube['sender'], cube['platform'], cube['signature'], cube['payload'])
                    updated_cubes.append(updated_cube)
                self._Blockchain__open_cubes = updated_cubes
                peer_nodes = json.loads(file_content[2])
                self._Blockchain__peer_nodes = set(peer_nodes)
        except (IOError, IndexError):
            pass
        finally:
            print('Cleanup!')

    def add_cube(self, sender, platform, signature, payload, is_receiving=False):
        """ Append a new value as well as the last blockchain value to the blockchain.
        Arguments:
            :sender: Tecihe sender of the coins.
            :rpient: The recipient of the coins.
            :amount: The amount of coins sent with the cube (default = 1.0)
        """
        cube = Citation(sender, platform, signature, payload)
        if Verification.verify_citation(cube):
            self._Blockchain__open_cubes.append(cube)
            self.save_data()
            if not is_receiving:
                for node in self.__peer_nodes:
                    url = 'http://{}/cube/broadcast-citation'.format(node)
                    try:
                        response = requests.post(url, json={
                                                 'sender': sender, 'recipient': recipient,  'signature': signature, 'amount': amount})
                        if response.status_code == 400 or response.status_code == 500:
                            print('Transaction declined, needs resolving')
                            return False
                    except requests.exceptions.ConnectionError:
                        continue
            return True
        return False

class FeedbackBlockchain(Blockchain):
    def __init__(self):
        super().__init__('fb')

    def add_cube(self, sender, platform, signature, payload, is_receiving=False):
        """ Append a new value as well as the last blockchain value to the blockchain.
        Arguments:
            :sender: Tecihe sender of the coins.
            :rpient: The recipient of the coins.
            :amount: The amount of coins sent with the cube (default = 1.0)
        """
        cube = Feedback(sender, platform, signature, payload)
        if Verification.verify_feedback(cube):
            self._Blockchain__open_cubes.append(cube)
            self.save_data()
            if not is_receiving:
                for node in self.__peer_nodes:
                    url = 'http://{}/cube/broadcast-feedback'.format(node)
                    try:
                        response = requests.post(url, json={
                                                 'sender': sender, 'recipient': recipient,  'signature': signature, 'amount': amount})
                        if response.status_code == 400 or response.status_code == 500:
                            print('Transaction declined, needs resolving')
                            return False
                    except requests.exceptions.ConnectionError:
                        continue
            return True
        return False


    def load_data(self):
        """Initialize blockchain + open cubes data from a file."""
        try:
            with open('fb_chain.txt', mode='r') as f:
                # file_content = pickle.loads(f.read())
                file_content = f.readlines()
                # blockchain = file_content['chain']
                # open_cubes = file_content['ot']
                blockchain = json.loads(file_content[0][:-1])
                # We need to convert  the loaded data because cubes should use OrderedDict
                updated_blockchain = []
                for block in blockchain:
                    converted_cube = [Feedback(
                        cube['sender'], cube['platform'], cube['signature'], cube['payload']) for cube in block['cubes']]
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                open_cubes = json.loads(file_content[1][:-1])
                # We need to convert  the loaded data because cubes should use OrderedDict
                updated_cubes = []
                for cube in open_cubes:
                    updated_cube = Feedback(
                        cube['sender'], cube['platform'], cube['signature'], cube['payload'])
                    updated_cubes.append(updated_cube)
                self._Blockchain__open_cubes = updated_cubes
                peer_nodes = json.loads(file_content[2])
                self._Blockchain__peer_nodes = set(peer_nodes)
        except (IOError, IndexError):
            pass
        finally:
            print('Cleanup!')


class FakeBlockchain(Blockchain):
    def __init__(self):
        super().__init__()

    def mine_block(self):
        """Create a new block and add open cubes to it."""
        # Fetch the currently last block of the blockchain
        if self.public_key == None:
            return None
        last_block = self.__chain[-1]
        # Hash the last block (=> to be able to compare it to the stored hash value)
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        # Miners should be rewarded, so let's create a reward cube
        # reward_cube = {
        #     'sender': 'MINING',
        #     'recipient': owner,
        #     'amount': MINING_REWARD
        # }
        reward_cube = Transaction(
            'MINING', self.public_key, '', MINING_REWARD)
        # Copy cube instead of manipulating the original open_cubes list
        # This ensures that if for some reason the mining should fail, we don't have the reward cube stored in the open cubes
        copied_cubes = self.__open_cubes[:]
        for tx in copied_cubes:
            if not Wallet.verify_cubes(tx, 'tx'):
                return None
        copied_cubes.append(reward_cube)
        block = Block(len(self.__chain), hashed_block,
                      copied_cubes, proof)
        self.__chain.append(block)
        self.__open_cubes = []
        self.save_data()
        for node in self.__peer_nodes:
            url = 'http://{}/block/broadcast'.format(node)
            converted_block = block.__dict__.copy()
            converted_block['cubes'] = [
                tx.__dict__ for tx in converted_block['cubes']]
            try:
                response = requests.post(url, json={'block': converted_block})
                if response.status_code == 400 or response.status_code == 500:
                    print('Block declined, needs resolving')
                if response.status_code == 409:
                    self.resolve_conflicts = True
            except requests.exceptions.ConnectionError:
                continue
        return block