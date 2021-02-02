"""Provides verification methods to verify the integrity of each chain"""
from transaction import Transaction, Citation, Feedback
from utility.hash_util import hash_string_265, hash_block
from wallet import Wallet
from collections.abc import Callable

class Verification:
    @staticmethod
    def valid_proof(cubes: list, last_hash: str, proof: str):
        """Ensures that a proof is valid to ensure the chain is legitimate.

        Args:
            cubes (list): List of cubes.
            last_hash (str): The last hash in the chain
            proof (str): The associated proof

        Returns:
            bool: If a proof is valid
        """
        guess = (str([cube.to_ordered_dict() for cube in cubes]) + str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_265(guess)
        print(guess_hash)
        return guess_hash[0:2] == '00'

    @classmethod
    def verify_chain(cls, blockchain):
        """Used to verify the integrity of the chain by checking each individual Cube and Block.

        Args:
            blockchain (list): list of all blocks in the blockchain.
        """
        # We can make it a little easier on functions that provide the blockchain by structuring the blockchain with Block Objects
        for (index, block) in enumerate(blockchain):
            if index == 0: # A previous hash cannot be checked.
                continue
            if block.previous_hash != hash_block(blockchain[index - 1]): # If the current hash and the previous hash do not match
                return False
            if not cls.valid_proof(block.cubes[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid and the chain cannot be verified')
                return False
        return True

    @staticmethod
    def verify_feedback(feedback: Feedback):
        """Used to verify if Feedback in the FbChain is valid.

        Args:

        Returns:
            bool: If the feedback can be verified.
        """
        return True

    @staticmethod
    def verify_citation(citation: Citation):
        """Used to verify if Feedback in the FbChain is valid.

        Args:

        Returns:
            bool: If the feedback can be verified.
        """
        return True

    @staticmethod
    def verify_transaction(transaction: Transaction, get_balance: Callable, check_funds: bool=True):
        """Used to verify if a Transaction in the TxChain is valid.

        Args:
            transaction (Transaction): The transaction payload containing the next Cube that will go in the block.
            get_balance (Callback[]): The callback function to check the sender's balance 
            check_funds (bool, optional): Whether the verification method should check for funds. Defaults to True.

        Returns:
            bool: If the transaction can be verified.
        """
        if check_funds:
            sender_balance = get_balance(cube.sender)
            return sender_balance >= cube.amount and Wallet.verify_transaction(transaction)
        else:
            return Wallet.verify_transaction(transaction)
    
    @classmethod
    def verify_transactions(cls, open_transactions: list, get_balance):
        """Used to verify all transactions in the TxChain.

        Args:
            open_transactions (list): [description]
            get_balance ([type]): [description]

        Returns:
            [type]: [description]
        """
        return all([cls.verify_transaction(tx, get_balance, False) for tx in open_transactions])