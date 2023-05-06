class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSubTree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)
