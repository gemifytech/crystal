from time import time
from utility.printable import Printable

class Block(Printable):
	def __init__(self, index, previous_hash, transactions, proof, timestamp = None):
		self.index = index
		self.previous_hash = previous_hash
		self.timestamp = time() if timestamp is None else timestamp
		self.transactions = transactions
		self.proof = proof

class FeedbackBlock(Printable):
    def __init__(self, index, previous_hash, feedbacks, proof, timestamp = None):
        self.index = index
		self.previous_hash = previous_hash
		self.timestamp = time() if timestamp is None else timestamp
		self.transactions = transactions
		self.proof = proof

class CitationBlock(Printable):
    def __init__(self, index, previous_hash, citations, proof, timestamp = None):
        self.index = index
		self.previous_hash = previous_hash
		self.timestamp = time() if timestamp is None else timestamp
		self.transactions = transactions
		self.proof = proof
