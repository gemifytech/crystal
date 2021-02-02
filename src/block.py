from time import time
from utility.printable import Printable

class Block(Printable):
    def __init__(self, index, previous_hash, cubes, proof, timestamp = None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time() if timestamp is None else timestamp
        self.cubes = cubes
        self.proof = proof