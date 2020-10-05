class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def is_bst(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.left.key > root.key:
        return False
    if root.right is not None and root.right.key < root.key:
        return False
    return is_bst(root.left) and is_bst(root.right)


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def larger(root_1, root_2):
    children_1 = count_nodes(root_1)
    children_2 = count_nodes(root_2)
    return root_1 if children_1 >= children_2 else root_2


def largest_bst_subtree(root):
    if is_bst(root):
        return root
    return larger(largest_bst_subtree(root.left), largest_bst_subtree(root.right))


#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))
# 749
