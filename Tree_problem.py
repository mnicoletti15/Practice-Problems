class BST:
    empty = ()
    def __init__(self, first, left=empty, right=empty):
        self.label = first
        self.left = left
        self.right = right
    def is_leaf(self):
        return (not self.left) and (not self.right)
    def __iter__(self):
        return elements(self)
    def contains(self, node):
        if self.is_leaf() and not self is node:
            return False
        elif self is node:
            return True
        else:
            return ((not (self.left is BST.empty)) and self.left.contains(node))\
                or ((not (self.right is BST.empty)) and self.right.contains(node))



def common_ancestor(tree, node1, node2):
    """Finds common ancestor of NODE1 and NODE2 in binary tree TREE.

    >>> t = BST(4, BST(8), BST(28))
    >>> t.left.left = BST(4, BST(3), BST(2))
    >>> t.left.right = BST(6)
    >>> a = common_ancestor(t, t.left.left.right, t.left.right)
    >>> a == t.left
    True
    """
    if tree.is_leaf:
        if node1 is node2 and node1 is tree:
            return tree
    if not (tree.contains(node1) and tree.contains(node2)):
        return None
    left = common_ancestor(tree.left, node1, node2)
    right = common_ancestor(tree.right, node1, node2)
    if left == None and right == None:
        return tree
    elif left == None:
        return right
    else:
        return left





def _test():
    import doctest
    doctest.testmod()
    
if __name__ == "__main__":
    _test()