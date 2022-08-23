from Practice2.Online_shop_practice import Shop


class Node:

    def __init__(self, data: Shop):
        self.data = data    # type: # Shop
        self.next = None    # type: # [Node, None]

    def has_value(self, value: Shop):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data