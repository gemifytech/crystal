from collections import OrderedDict
from utility.printable import Printable


class Cube(Printable):
	"""The foundation for the any type of activity that happens in each individual Blockchain
	"""
	def __init__(self, sender, signature, type: str):
		self.sender = sender
		self.signature = signature
		self.type = type


class Transaction(Cube):
	"""The building block for activity within the TransactionChain
	"""
	def __init__(self, sender, recipient, signature, amount):
		super().__init__(sender, signature, 'tx')
		self.recipient = recipient
		self.amount = amount

	def to_ordered_dict(self):
		return OrderedDict([('sender',self.sender),('recipient',self.recipient),('amount',self.amount)])


class Feedback(Cube):
	"""The building block for activity within the TransactionChain
	"""
    def __init__(self, sender, platform, signature, package):
		super().__init__(sender, signature, 'fb')
        self.platform = platform 
        self.package = package

    def to_ordered_dict(self):
		# Might not need to include the platform that is included. Revise this.
		return OrderedDict([('sender',self.sender),('platform',self.platform),('package',self.package)])

	def validate_package(self):
		return False


class Citation(Cub):
	"""The building block for activity within the TransactionChain
	"""
    def __init__(self, sender, platform, signature, package):
		super().__init__(sender, signature, 'ct')
        self.platform = platform
        self.package = package

    def to_ordered_dict(self):
		return OrderedDict([('sender',self.sender),('platform',self.platform),('package',self.package)])

	def validate_package(self):
		return False