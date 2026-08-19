# LC3. Check if Binary Tree is BST
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root:
        return True
    if root.val <= lo or root.val >= hi:
        return False
    return is_valid_bst(root.left, lo, root.val) and is_valid_bst(root.right, root.val, hi)

if __name__ == "__main__":
    # Example: valid BST [2,1,3]
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(is_valid_bst(root))
