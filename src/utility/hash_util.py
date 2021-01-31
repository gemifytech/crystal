import hashlib as hl
import json

def hash_string_265(string):
	return hl.sha256(string).hexdigest()

def hash_block(block):
	hashable_block = block.__dict__.copy() # Important to keep copy at the end so previous block does not get overwritten.
	hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
	return hash_string_265(json.dumps(hashable_block, sort_keys=True).encode())