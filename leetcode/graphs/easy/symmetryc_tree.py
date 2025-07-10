from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:

    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root, root)

def is_symmetric_iterative(root: Optional[TreeNode]) -> bool:

    if not root:
        return True

    queue = deque([(root.left, root.right)])
    while queue:
        left, right = queue.popleft()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True


def build_tree(level_vals):
    """
    Build a binary tree from a level-order list.
    Use None for missing children.
    """
    if not level_vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in level_vals]
    kids = nodes[::-1]  # start from the end for pop()
    root = kids.pop()  # first element is the root
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def run_tests():
    test_cases = [
        ("Empty tree", []),
        ("Single node", [1]),
        ("Perfectly symmetric", [1, 2, 2, 3, 4, 4, 3]),
        ("Asymmetric – missing node", [1, 2, 2, None, 3, None, 3]),
        ("Asymmetric – different values", [1, 2, 2, 3, 5, 4, 3]),
    ]

    for name, arr in test_cases:
        root = build_tree(arr)
        result = is_symmetric_iterative(root)
        print(f"{name:28s}: {result}")


if __name__ == "__main__":
    run_tests()
