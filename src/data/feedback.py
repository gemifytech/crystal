from collections import OrderedDict
from utility.printable import Printable


class Feedback(Printable):
    def __init__(self, sender, platform, signature, package):
        self.sender = sender
        self.platform = platform
        self.signature = signature
        self.package = package

    def to_ordered_dict(self):
		return OrderedDict([('sender',self.sender),('platform',self.platform),('package',self.package)])
