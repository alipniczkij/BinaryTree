
class TreeNode(object):
    """
    Node for Tree
    """
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

        values_check = isinstance(value, (int, float)) and 
                        (isinstance(left, TreeNode) or left is None) and 
                        (isinstance(right, TreeNode) or right is None)

        if not values_check:
            raise ValueError

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __iter__(self):
        cur = [self]
        while cur:
            next = []
            for node in cur:
                yield node
                if node.right:
                    next.append(node.right)
                if node.left:
                    next.append(node.left)
            cur = next

    def count(self):
        return sum([1 for _ in self])

    def __getitem__(self, index):
        if not 0 <= index < self.count():
            raise IndexError
    
    def __setitem__(self, index, node):
        pass

    def __setattr__(self, attr, val):
        pass

    def __delitem__(self, index):
        pass

    def __eq__(self, other):
        if type(other) is TreeNode:
            return self.value == other.value
        return self.value == other

    def __ne__(self, other):
        return not self == other

    def height(self):
        pass

    def is_balanced(self):
        pass

    def is_bst(self):
        pass

    def is_symmetric(self):
        pass

