class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_unival(root):
    if root is None:
        return True
    if root.left is not None and root.left.val != root.val:
        return False
    if root.right is not None and root.right.val != root.val:
        return False
    return is_unival(root.left) and is_unival(root.right)

def count_unival_subtrees(root):
    if root.left is None and root.right is None:
        return 1
    if is_unival(root):
        return 1 + count_unival_subtrees(root.left) + count_unival_subtrees(root.right)
    return count_unival_subtrees(root.left) + count_unival_subtrees(root.right)


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)
"""
   0
  / \
 1   0
    / \
   1   0
  / \
 1   0
"""
print(count_unival_subtrees(a))
# 5
