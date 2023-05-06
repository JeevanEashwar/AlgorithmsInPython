class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    # Create inverted left and right objects
    inverted_left = invertTree(root.left)
    inverted_right = invertTree(root.right)

    root.left = inverted_right
    root.right = inverted_left

    return root
