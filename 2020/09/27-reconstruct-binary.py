from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def find_root(preorder, inorder):
    for val in preorder:
        if val in inorder:
            return val
    return None


def reconstruct(preorder, inorder):
    # Scan pre-order ltr to get root of current in-order array
    root_val = find_root(preorder, inorder)
    root = None
    if root_val is not None:
        root = Node(root_val)
        # Split in-order left and right subtree at determined root
        root_index = inorder.index(root_val)
        root.left = reconstruct(preorder, inorder[:root_index])
        root.right = reconstruct(preorder, inorder[root_index + 1:])
    return root


"""
    a
   / \
  b   c
 / \ / \
d  e f  g
"""
tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree)
# abcdefg
